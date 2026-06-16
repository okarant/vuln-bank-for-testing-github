from flask import jsonify, request
import jwt
import datetime
import os
import re
import secrets
import sqlite3
import time
from collections import defaultdict
from functools import wraps

from werkzeug.security import generate_password_hash, check_password_hash

from database import execute_query


def _load_jwt_secret():
    """Load the JWT signing secret from the environment.

    Falls back to an ephemeral, process-local random secret when the variable
    is absent so the application never ships with a predictable hardcoded key.
    """
    secret = os.environ.get("JWT_SECRET")
    if not secret:
        secret = secrets.token_urlsafe(64)
        print(
            "WARNING: JWT_SECRET is not set. Generated an ephemeral signing key; "
            "set JWT_SECRET in the environment for stable, production-grade tokens."
        )
    return secret


JWT_SECRET = _load_jwt_secret()

# Only a single strong HMAC algorithm is accepted. Unsigned ('none') tokens are never allowed.
ALGORITHMS = ['HS256']

# Access/ID token lifetime (seconds).
TOKEN_TTL_SECONDS = int(os.environ.get("JWT_TTL_SECONDS", "3600"))

# Minimum password policy shared by end users AND server-to-server/system accounts.
MIN_PASSWORD_LENGTH = 12


def validate_password_policy(password):
    """Return (ok, message). Single shared baseline for ALL account types."""
    if not password or len(password) < MIN_PASSWORD_LENGTH:
        return False, f"Password must be at least {MIN_PASSWORD_LENGTH} characters long"
    classes = [r'[a-z]', r'[A-Z]', r'\d', r'[^A-Za-z0-9]']
    if sum(1 for pattern in classes if re.search(pattern, password)) < 3:
        return False, "Password must combine at least three of: lowercase, uppercase, digits, symbols"
    return True, ""


def hash_password(password):
    """Salt and hash a password with PBKDF2-HMAC-SHA256 (per-password random salt)."""
    return generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)


def verify_password(stored_hash, provided_password):
    """Constant-time verification of a provided password against a stored hash."""
    if not stored_hash or provided_password is None:
        return False
    try:
        return check_password_hash(stored_hash, provided_password)
    except Exception:
        return False


def hash_token(raw_token):
    """One-way hash for storing OTP/reset PINs and API tokens at rest."""
    return generate_password_hash(raw_token, method='pbkdf2:sha256', salt_length=16)


def verify_hashed_token(stored_hash, provided_token):
    if not stored_hash or provided_token is None:
        return False
    try:
        return check_password_hash(stored_hash, provided_token)
    except Exception:
        return False


def generate_secure_pin(digits=6):
    """Cryptographically secure numeric one-time PIN."""
    upper = 10 ** digits
    return str(secrets.randbelow(upper)).zfill(digits)


def generate_api_token(nbytes=32):
    """Cryptographically secure, high-entropy access/API token (>=128 bits)."""
    return secrets.token_urlsafe(nbytes)


# ---- Account lockout / authentication throttling (in-memory) ----
_failed_auth = defaultdict(list)
LOCKOUT_THRESHOLD = int(os.environ.get("AUTH_LOCKOUT_THRESHOLD", "5"))
LOCKOUT_WINDOW_SECONDS = int(os.environ.get("AUTH_LOCKOUT_WINDOW", str(15 * 60)))


def _prune_failures(key, now):
    _failed_auth[key] = [ts for ts in _failed_auth[key] if ts > now - LOCKOUT_WINDOW_SECONDS]


def is_locked_out(key):
    now = time.time()
    _prune_failures(key, now)
    return len(_failed_auth[key]) >= LOCKOUT_THRESHOLD


def record_failed_auth(key):
    now = time.time()
    _prune_failures(key, now)
    _failed_auth[key].append(now)


def reset_failed_auth(key):
    _failed_auth.pop(key, None)


def generate_token(user_id, username, is_admin=False):
    """Generate a signed JWT access token with issue/expiry claims."""
    now = datetime.datetime.utcnow()
    payload = {
        'user_id': user_id,
        'username': username,
        'is_admin': is_admin,
        'iat': now,
        'exp': now + datetime.timedelta(seconds=TOKEN_TTL_SECONDS)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm='HS256')


def verify_token(token):
    """Verify a JWT token's signature and expiry. Never accepts unsigned tokens."""
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=ALGORITHMS)
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    except Exception:
        return None


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        # Try to get token from Authorization header
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                # Handle 'Bearer' token format
                if 'Bearer' in auth_header:
                    token = auth_header.split(' ')[1]
                else:
                    token = auth_header
            except IndexError:
                token = None
                
        # Access tokens are accepted only from the Authorization header or an
        # httponly cookie. They are never read from query-string/form parameters
        # because those are cached by proxies and leak into logs/history.
        if not token and 'token' in request.cookies:
            token = request.cookies['token']
            
        if not token:
            return jsonify({'error': 'Token is missing'}), 401

        try:
            current_user = verify_token(token)
            if current_user is None:
                return jsonify({'error': 'Invalid token'}), 401
                
            return f(current_user, *args, **kwargs)
            
        except Exception as e:
            return jsonify({
                'error': 'Invalid token', 
                'details': str(e)
            }), 401
            
    return decorated

# New API endpoints with JWT authentication
def init_auth_routes(app):
    @app.route('/api/login', methods=['POST'])
    def api_login():
        auth = request.get_json()
        suspension_message = 'Your account has been suspended, contact support or walk in to any of our branch to resolve the issue'

        if not auth or not auth.get('username') or not auth.get('password'):
            return jsonify({'error': 'Missing credentials'}), 401

        username = auth.get('username')
        lock_key = f"login:{username}"
        if is_locked_out(lock_key):
            return jsonify({'error': 'Account temporarily locked due to repeated failed attempts. Try again later.'}), 429

        # Parameterized query (no SQL injection); password is verified against a
        # salted PBKDF2 hash rather than compared in plaintext SQL.
        rows = execute_query("SELECT * FROM users WHERE username = %s", (username,))
        user = rows[0] if rows else None

        if not user or not verify_password(user[2], auth.get('password')):
            record_failed_auth(lock_key)
            return jsonify({'error': 'Invalid credentials'}), 401

        if len(user) > 9 and user[9]:
            return jsonify({'error': suspension_message}), 403

        reset_failed_auth(lock_key)
        token = generate_token(user[0], user[1], user[5])

        return jsonify({
            'token': token,
            'user_id': user[0],
            'username': user[1],
            'account_number': user[3],
            'is_admin': user[5]
        })

    @app.route('/api/check_balance', methods=['GET'])
    @token_required
    def api_check_balance(current_user):
        # Any valid token can check any account balance
        account_number = request.args.get('account_number')
        
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()
        c.execute(f"SELECT username, balance FROM users WHERE account_number='{account_number}'")
        user = c.fetchone()
        conn.close()
        
        if user:
            return jsonify({
                'username': user[0],
                'balance': user[1],
                'checked_by': current_user['username']
            })
        return jsonify({'error': 'Account not found'}), 404

    @app.route('/api/transfer', methods=['POST'])
    @token_required
    def api_transfer(current_user):
        data = request.get_json()
        
        if not data or not data.get('to_account') or not data.get('amount'):
            return jsonify({'error': 'Missing transfer details'}), 400
            
        amount = float(data.get('amount'))
        to_account = data.get('to_account')
        
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()
        
        c.execute(f"SELECT balance FROM users WHERE id={current_user['user_id']}")
        balance = c.fetchone()[0]
        
        if balance >= amount:
            c.execute(f"UPDATE users SET balance = balance - {amount} WHERE id={current_user['user_id']}")
            c.execute(f"UPDATE users SET balance = balance + {amount} WHERE account_number='{to_account}'")
            conn.commit()
            
            c.execute(f"SELECT username, balance FROM users WHERE account_number='{to_account}'")
            recipient = c.fetchone()
            
            conn.close()
            return jsonify({
                'status': 'success',
                'new_balance': balance - amount,
                'recipient': recipient[0],
                'recipient_new_balance': recipient[1]
            })
            
        conn.close()
        return jsonify({'error': 'Insufficient funds'}), 400

import os
import secrets
import psycopg2
from psycopg2 import pool
from datetime import datetime
import time

from werkzeug.security import generate_password_hash

# Database credentials are sourced exclusively from the environment. No plaintext
# password is embedded as a default; a missing DB_PASSWORD fails fast at connect time
# rather than silently falling back to a well-known value.
DB_CONFIG = {
    'dbname': os.getenv('DB_NAME', 'vulnerable_bank'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.environ.get('DB_PASSWORD', ''),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432')
}

# Create a connection pool
connection_pool = None

def init_connection_pool(min_connections=2, max_connections=30, max_retries=5, retry_delay=2):
    """Initialize the database connection pool with retry mechanism."""
    global connection_pool
    if connection_pool is not None:
        return connection_pool

    retry_count = 0
    
    while retry_count < max_retries:
        try:
            connection_pool = psycopg2.pool.ThreadedConnectionPool(
                min_connections,
                max_connections,
                **DB_CONFIG
            )
            print("Database connection pool created successfully")
            return connection_pool
        except Exception as e:
            retry_count += 1
            print(f"Failed to connect to database (attempt {retry_count}/{max_retries}): {e}")
            if retry_count < max_retries:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print("Max retries reached. Could not establish database connection.")
                raise e

def check_database_connection():
    conn = None
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        return True
    except Exception as e:
        print(f"Database health check failed: {e}")
        return False
    finally:
        if conn:
            return_connection(conn)

def get_connection():
    if not connection_pool:
        raise Exception("Connection pool not initialized")

    max_attempts = max(1, int(os.getenv('DB_POOL_CHECKOUT_ATTEMPTS', '3')))
    retry_delay = float(os.getenv('DB_POOL_CHECKOUT_RETRY_DELAY', '0.2'))

    for attempt in range(1, max_attempts + 1):
        try:
            return connection_pool.getconn()
        except pool.PoolError as e:
            if attempt >= max_attempts:
                raise e

            print(
                "Database connection pool exhausted "
                f"(attempt {attempt}/{max_attempts}); retrying in {retry_delay} seconds"
            )
            time.sleep(retry_delay)

def return_connection(connection):
    if connection_pool:
        connection_pool.putconn(connection)

def init_db():
    """Initialize database tables."""
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # Create users table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    account_number TEXT NOT NULL UNIQUE,
                    balance DECIMAL(15, 2) DEFAULT 1000.0,
                    is_admin BOOLEAN DEFAULT FALSE,
                    profile_picture TEXT,
                    reset_pin TEXT,
                    bio TEXT,
                    is_suspended BOOLEAN DEFAULT FALSE
                )
            ''')

            # Migration: Add bio column if it doesn't exist (for existing databases)
            try:
                cursor.execute("ALTER TABLE users ADD COLUMN IF NOT EXISTS bio TEXT")
            except Exception:
                pass  # Column already exists or error adding it

            try:
                cursor.execute("ALTER TABLE users ADD COLUMN IF NOT EXISTS is_suspended BOOLEAN DEFAULT FALSE")
            except Exception:
                pass  # Column already exists or error adding it

            # Expiry timestamp for password-reset PINs (one-time, short-lived).
            try:
                cursor.execute("ALTER TABLE users ADD COLUMN IF NOT EXISTS reset_pin_expiry TIMESTAMP")
            except Exception:
                pass  # Column already exists or error adding it
            
            # Create loans table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS loans (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                    amount DECIMAL(15, 2),
                    status TEXT DEFAULT 'pending'
                )
            ''')
            
            # Create transactions table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS transactions (
                    id SERIAL PRIMARY KEY,
                    from_account TEXT NOT NULL,
                    to_account TEXT NOT NULL,
                    amount DECIMAL(15, 2) NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    transaction_type TEXT NOT NULL,
                    description TEXT
                )
            ''')
            
            # Create virtual cards table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS virtual_cards (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                    card_number TEXT NOT NULL UNIQUE,
                    cvv TEXT NOT NULL,
                    expiry_date TEXT NOT NULL,
                    card_limit NUMERIC(20, 8) DEFAULT 1000.0,
                    current_balance NUMERIC(20, 8) DEFAULT 0.0,
                    is_frozen BOOLEAN DEFAULT FALSE,
                    is_active BOOLEAN DEFAULT TRUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_used_at TIMESTAMP,
                    card_type TEXT DEFAULT 'standard',
                    currency TEXT DEFAULT 'USD'
                )
            ''')

            # Create virtual card transactions table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS card_transactions (
                    id SERIAL PRIMARY KEY,
                    card_id INTEGER REFERENCES virtual_cards(id) ON DELETE CASCADE,
                    amount NUMERIC(20, 8) NOT NULL,
                    merchant_name TEXT,
                    transaction_type TEXT NOT NULL,
                    status TEXT DEFAULT 'pending',
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    description TEXT
                )
            ''')

            # Create merchants table for payment APIs
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS merchants (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL,
                    api_key TEXT NOT NULL,
                    is_active BOOLEAN DEFAULT TRUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            # Create merchant payments table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS merchant_payments (
                    id SERIAL PRIMARY KEY,
                    merchant_id INTEGER REFERENCES merchants(id) ON DELETE CASCADE,
                    card_id INTEGER REFERENCES virtual_cards(id) ON DELETE SET NULL,
                    amount NUMERIC(20, 8) NOT NULL,
                    currency TEXT DEFAULT 'USD',
                    status TEXT DEFAULT 'pending',
                    merchant_order_id TEXT,
                    authorization_code TEXT,
                    failure_reason TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            # Seed demo merchants WITHOUT hardcoded credentials. Each seeded account
            # gets a salted+hashed password (sourced from the environment when
            # provided, otherwise a strong random secret generated at install time)
            # and a high-entropy random API key. Existing rows keep their stored
            # credentials so secrets are not rotated/regenerated on every startup.
            seeded_merchant_specs = [
                ('graphQL bookstore', 'bookstore@vulnbank.org'),
                ('PwnShop', 'pwnshop@vulnbank.org'),
            ]
            for name, email in seeded_merchant_specs:
                cursor.execute("SELECT id FROM merchants WHERE email = %s", (email,))
                if cursor.fetchone():
                    cursor.execute(
                        """
                        UPDATE merchants
                        SET name = %s, is_active = %s
                        WHERE email = %s
                        """,
                        (name, True, email)
                    )
                else:
                    env_slug = email.split('@')[0].upper().replace('.', '_')
                    raw_password = os.environ.get(f"MERCHANT_{env_slug}_PASSWORD") or secrets.token_urlsafe(18)
                    hashed_password = generate_password_hash(raw_password, method='pbkdf2:sha256', salt_length=16)
                    api_key = f"vk_{secrets.token_hex(32)}"
                    cursor.execute(
                        """
                        INSERT INTO merchants (name, email, password, api_key, is_active)
                        VALUES (%s, %s, %s, %s, %s)
                        """,
                        (name, email, hashed_password, api_key, True)
                    )

            try:
                cursor.execute("ALTER TABLE virtual_cards ADD COLUMN IF NOT EXISTS currency TEXT DEFAULT 'USD'")
            except Exception:
                pass

            try:
                cursor.execute("ALTER TABLE virtual_cards ALTER COLUMN card_limit TYPE NUMERIC(20, 8)")
                cursor.execute("ALTER TABLE virtual_cards ALTER COLUMN current_balance TYPE NUMERIC(20, 8)")
                cursor.execute("ALTER TABLE card_transactions ALTER COLUMN amount TYPE NUMERIC(20, 8)")
            except Exception:
                pass
            
            # Create the admin account if it doesn't exist, WITHOUT a hardcoded default
            # password. The password is taken from ADMIN_PASSWORD when set; otherwise a
            # strong random secret is generated at install time and stored salted+hashed.
            # The plaintext is never persisted or printed.
            cursor.execute("SELECT * FROM users WHERE username='admin'")
            if not cursor.fetchone():
                admin_password = os.environ.get('ADMIN_PASSWORD')
                if not admin_password:
                    admin_password = secrets.token_urlsafe(24)
                    print(
                        "WARNING: ADMIN_PASSWORD not set. Generated a random admin password "
                        "(not printed). Use the password-reset flow to set a known credential."
                    )
                cursor.execute(
                    """
                    INSERT INTO users (username, password, account_number, balance, is_admin) 
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (
                        'admin',
                        generate_password_hash(admin_password, method='pbkdf2:sha256', salt_length=16),
                        'ADMIN001',
                        1000000.0,
                        True,
                    )
                )
            
            # Create bill categories table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS bill_categories (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL UNIQUE,
                    description TEXT,
                    is_active BOOLEAN DEFAULT TRUE
                )
            ''')

            # Create billers table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS billers (
                    id SERIAL PRIMARY KEY,
                    category_id INTEGER REFERENCES bill_categories(id),
                    name TEXT NOT NULL,
                    account_number TEXT NOT NULL,
                    description TEXT,
                    minimum_amount DECIMAL(15, 2) DEFAULT 0,
                    maximum_amount DECIMAL(15, 2),
                    is_active BOOLEAN DEFAULT TRUE
                )
            ''')

            # Create bill payments table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS bill_payments (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                    biller_id INTEGER REFERENCES billers(id),
                    amount DECIMAL(15, 2) NOT NULL,
                    payment_method TEXT NOT NULL,  -- 'balance' or 'virtual_card'
                    card_id INTEGER REFERENCES virtual_cards(id),  -- NULL if paid with balance
                    reference_number TEXT,
                    status TEXT DEFAULT 'pending',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    processed_at TIMESTAMP,
                    description TEXT
                )
            ''')

            # Insert default bill categories
            cursor.execute("""
                INSERT INTO bill_categories (name, description) 
                VALUES 
                ('Utilities', 'Water, Electricity, Gas bills'),
                ('Telecommunications', 'Phone, Internet, Cable TV'),
                ('Insurance', 'Life, Health, Auto insurance'),
                ('Credit Cards', 'Credit card bill payments')
                ON CONFLICT (name) DO NOTHING
            """)

            # Insert sample billers
            cursor.execute("""
                INSERT INTO billers (category_id, name, account_number, description, minimum_amount) 
                VALUES 
                (1, 'City Water', 'WATER001', 'City Water Utility', 10),
                (1, 'PowerGen Electric', 'POWER001', 'Electricity Provider', 20),
                (2, 'TeleCom Services', 'TEL001', 'Phone and Internet', 25),
                (2, 'CableTV Plus', 'CABLE001', 'Cable TV Services', 30),
                (3, 'HealthFirst Insurance', 'INS001', 'Health Insurance', 100),
                (4, 'Universal Bank Card', 'CC001', 'Credit Card Payments', 50)
                ON CONFLICT DO NOTHING
            """)
            
            conn.commit()
            print("Database initialized successfully")
            
    except Exception as e:
        print(f"Error initializing database: {e}")
        conn.rollback()
        raise e
    finally:
        return_connection(conn)

def execute_query(query, params=None, fetch=True):
    """Execute a database query."""
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            result = None
            if fetch:
                result = cursor.fetchall()
            # Always commit for INSERT, UPDATE, DELETE operations
            if query.strip().upper().startswith(('INSERT', 'UPDATE', 'DELETE')):
                conn.commit()
            return result
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        return_connection(conn)

def execute_transaction(queries_and_params):
    """Execute multiple queries in a transaction.
    queries_and_params: list of tuples (query, params)
    """
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            for query, params in queries_and_params:
                cursor.execute(query, params)
            conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        return_connection(conn)

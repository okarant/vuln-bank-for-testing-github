# VulnBank

A full-featured banking web application with user accounts, transfers, virtual cards, merchant payments, bill pay, and an AI-powered customer support agent.

## Features

### Core Banking
- User authentication and authorization
- Account balance management
- Money transfers between accounts
- Loan requests
- Profile picture upload
- Transaction history
- Transaction analytics dashboard (GraphQL-backed)
- Password reset system
- Multi-currency virtual cards management
- Virtual card funding with built-in currency conversion (USD, GBP, NGN, JPY, EUR, QAR, BTC, ETH)
- Public merchant payment API for ecommerce integrations
- Bill payments system
- AI customer support agent (DeepSeek API / mock mode)

## Installation & Setup

### Prerequisites
- Docker and Docker Compose (for containerized setup)
- PostgreSQL (if running locally)
- Python 3.9 or higher (for local setup)
- Git

### Option 1: Using Docker (Recommended)

#### Using Docker Compose (Easiest)

1. Clone the repository:
```bash
git clone <repo-url>
cd vuln-bank
```

2. Start the application:
```bash
docker-compose up -d --build
```

The application will be available at `http://localhost:5000`

#### Container recovery behavior
The Docker setup includes operational safeguards so the app can recover without manual intervention:
- `web` and `db` use `restart: unless-stopped`, so Docker restarts them automatically if the process exits.
- `db` exposes a health check, and `web` waits for Postgres readiness before starting.
- `web` runs the Flask development server with `debug=True`.
- `web` exposes `GET /healthz` so the container can report whether the app and database are actually usable.

#### Local smoke test
You can validate the local runtime wiring without starting real containers:
```bash
python3 -m unittest discover -s tests -v
```

#### Using Docker Only

1. Clone the repository:
```bash
git clone <repo-url>
cd vuln-bank
```

2. Build the Docker image:
```bash
docker build -t vuln-bank .
```

3. Run the container:
```bash
docker run -p 5000:5000 vuln-bank
```

### Option 2: Local Installation

#### Prerequisites
- Python 3.9 or higher
- PostgreSQL installed and running
- pip (Python package manager)
- Git

#### Steps

1. Clone the repository:
```bash
git clone <repo-url>
cd vuln-bank
```

2. Create and activate a virtual environment (recommended):
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create necessary directories:
```bash
# On Windows
mkdir static\uploads

# On Linux/Mac
mkdir -p static/uploads
```

5. Modify the .env file:
   - Open .env and change DB_HOST from 'db' to 'localhost' for local PostgreSQL connection

6. Run the application:
```bash
# On Windows
python app.py

# On Linux/Mac
python3 app.py
```

### Environment Variables

Current environment variables:
```bash
DB_NAME=vulnerable_bank
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db  # Change to 'localhost' for local installation
DB_PORT=5432
```

### Database Setup
The application uses PostgreSQL. The database will be automatically initialized when you first run the application, creating:
- Users table
- Transactions table
- Loans table

### Accessing the Application
- Main application: `http://localhost:5000`
- API documentation: `http://localhost:5000/api/docs`
- GraphQL analytics endpoint: `http://localhost:5000/graphql`
- Admin analytics view: available from the admin dashboard after login as an admin user

### Common Issues & Solutions

#### Windows
1. If you get "python not found":
   - Ensure Python is added to your system PATH
   - Try using `py` instead of `python`

2. Permission issues with uploads folder:
   - Run command prompt as administrator
   - Ensure you have write permissions in the project directory

#### Linux/Mac
1. Permission denied when creating directories:
   ```bash
   sudo mkdir -p static/uploads
   sudo chown -R $USER:$USER static/uploads
   ```

2. Port 5000 already in use:
   ```bash
   sudo lsof -i:5000
   sudo kill <PID>
   ```

#### PostgreSQL Issues

1. Connection refused:
   * Ensure PostgreSQL is running
   * Check credentials in `.env` file
   * Verify PostgreSQL port is not blocked

2. Authentication failed:
   * Make sure `DB_PASSWORD` in `.env` matches your Postgres user's password.

3. Database does not exist:
   * Create it manually:
     ```bash
     createdb -U postgres -h localhost vulnerable_bank
     ```

## Contributing

Contributions are welcome! Feel free to:
- Add new features
- Improve existing functionality
- Enhance documentation
- Fix bugs

## License

This project is licensed under the MIT License - see the LICENSE file for details.

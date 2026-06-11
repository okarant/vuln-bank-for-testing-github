# Survey Evidence Log

## Codebase Analysis Summary
- **Language:** Python 3.9 (Flask)
- **Database:** PostgreSQL 13 (via psycopg2-binary)
- **Authentication:** JWT (pyjwt), custom token_required decorator
- **API:** REST endpoints, GraphQL (graphene)
- **AI:** DeepSeek LLM integration
- **Container:** Docker + Docker Compose
- **File Uploads:** Profile picture upload (multipart + URL fetch)
- **Docs:** Swagger UI (flask-swagger-ui)
- **CORS:** flask-cors enabled
- **Data Formats:** JSON (primary), YAML (docker-compose)
- **Version Control:** GitHub
- **OS Target:** Linux (Docker python:3.9-slim)

## Answers Selected (27 total, 22 newly applied)

| Answer ID | Question | Evidence |
|-----------|----------|----------|
| A4 | Components: Web application | Flask app serving HTML templates |
| A6 | Components: Web service | REST API endpoints (/api/*) |
| A1078 | Uses a database | PostgreSQL via psycopg2-binary |
| A1084 | Uses third-party libraries | Flask, JWT, Graphene, etc. |
| A1142 | Network communication | Web <-> DB over Docker network |
| A1350 | Include activity phase CMs | Financial app with broad attack surface |
| A759 | Financial application | Banking app: transfers, loans, cards |
| A1093 | Payment via service provider | Bill payments, merchant payments |
| A1152 | Linux/Unix | Docker python:3.9-slim (Debian) |
| A707 | Python | Main language (app.py, auth.py, etc.) |
| A3 | JavaScript | Frontend templates use JS |
| A1621 | Bash/Shell | start.sh script |
| A2302 | Reads/writes data files | File uploads (profile pictures) |
| A733 | JSON | Primary API format |
| A1285 | YAML | docker-compose.yml |
| A758 | Direct authentication | JWT-based user auth |
| A23 | Authorizes subjects | Admin vs regular user roles |
| A1140 | Forwards to remote services | AI agent calls DeepSeek API |
| A1362 | Uses LLMs | DeepSeek integration |
| A2307 | Receives text input | All form inputs, chat messages |
| A39 | File upload/transfer | Profile picture upload |
| A1143 | Generates random numbers | PINs, card numbers, CVVs |
| A21 | Passwords in config | JWT_SECRET="secret123" in source |
| A27 | Uses encryption (not SSL) | JWT token generation |
| A1390 | GitHub | Repository on GitHub |
| A1208 | Docker | Dockerfile + docker-compose.yml |
| A130 | Handles personal data | User accounts, banking data |

## Pre-selected answers (retained)
- A734, A735, A736, A737, A738, A739, A742, A1294, A1307, A1626

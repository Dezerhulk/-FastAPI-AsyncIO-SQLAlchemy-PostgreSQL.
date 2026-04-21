# -FastAPI-A
- SQLite/PostgreSQL persistence via `DATABASE_URL`
- Task statuses: `pending`, `processing`, `done`, `error`
- JWT authentication with username/password
- Rate limiting
- Background worker with error handling
- Configurable settings via `.env`
- Requeues pending and processing tasks from the database on startup

## Run locally

1. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and adjust values:

```bash
copy .env.example .env
```

4. Start the API:

```bash
python main.py
```

Or directly with uvicorn:

```bash
uvicorn task_api:app --reload
```

## Run tests

```bash
pytest -q
```

## Docker

Build and run the container directly:

```bash
docker build -t task-api .
docker run --rm -p 8000:8000 --env-file .env task-api
```

Or use Docker Compose for local development and live reload of the project volume:

```bash
docker compose up --build
```

The `docker-compose.yml` file mounts the project folder into `/app`, passes `.env` into the container, and exposes port `8000`.

## Environment variables

Use `.env` or environment variables to configure the service.

```env
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///./tasks.db
# For PostgreSQL, use a URL like:
# DATABASE_URL=postgresql://user:password@localhost:5432/task_db
RATE_LIMIT=5
ACCESS_TOKEN_EXPIRE_SECONDS=3600
LOG_FILE=app.log
```

## API Endpoints

### Authentication

- `POST /register` - register a new user (returns JWT token)
- `POST /login` - login with username and password (returns JWT token)

### Tasks

- `POST /tasks` - create a task (requires Bearer token)
- `GET /tasks/{task_id}` - check task status and result (requires Bearer token)

## Example requests

### 1. Register a new user:

```bash
curl -X POST http://localhost:8000/register \
  -H "Content-Type: application/json" \
  -d '{"username": "alice", "password": "alice123"}'
```

Response:

```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer"
}
```

### 2. Login:

```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "alice", "password": "alice123"}'
```

Response:

```json
syncIO-SQLAlchemy-PostgreSQL.

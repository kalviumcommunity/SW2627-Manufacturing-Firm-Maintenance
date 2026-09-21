# Manufacturing Floor Assistant Backend

Initial FastAPI scaffold for the Manufacturing Floor Assistant.

## Run locally

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The interactive API documentation is available at `http://127.0.0.1:8000/docs`.

## Current endpoint

- `GET /health` returns `{"status": "ok"}`.

Domain models, simulated records, troubleshooting routes, and automated API tests are scheduled for later days.

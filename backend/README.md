# Manufacturing Floor Assistant Backend

FastAPI service for source-referenced troubleshooting using fictional equipment manuals, maintenance logs, and safety procedures.

## Run locally

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The interactive API documentation is available at `http://127.0.0.1:8000/docs`.

## API

All new frontend-facing endpoints use `/api/v1`:

- `GET /api/v1/health` returns service status and version.
- `GET /api/v1/equipment` lists seeded machines.
- `GET /api/v1/equipment/{equipment_id}` returns machine context and source inventory.
- `GET /api/v1/search?q=conveyor%20overheating&limit=5` returns ranked source excerpts.
- `POST /api/v1/assistant/query` returns a deterministic troubleshooting response with source references.

Example assistant request:

```json
{
  "question": "The conveyor motor is overheating. What should I check?",
  "equipment_id": "conveyor-01",
  "limit": 5
}
```

Responses prioritize safety procedures for lockout, guarding, electrical, inspection, and jam-clearance queries. If no relevant source is found, the service returns a low-confidence escalation response instead of inventing a repair.

The original `/health`, `/machines`, and `/guidance` routes remain available for compatibility with the first scaffold.

## Test

From the repository root:

```bash
pytest
```

The service uses in-memory fictional data. It does not require a database, external LLM, API key, or vector-search service.

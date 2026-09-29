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

## Day 2 contract models

The typed contract in `app/schemas.py` defines the payloads that later routes will use:

- `Equipment` for machine identity, area, and operational status.
- `ManualDocument`, `MaintenanceLog`, and `SafetyProcedure` for source records.
- `SearchRequest` and `SearchResponse` for bounded source search.
- `AssistantQuery` and `AssistantResponse` for source-referenced troubleshooting.
- `SourceExcerpt` for consistent source attribution.
- `ErrorResponse` for stable nested error details.

Search questions are limited to 3-500 characters, result limits to 1-10, and document types to `manual`, `maintenance_log`, or `safety_procedure`.

## Day 3 seed data

The in-memory source data lives in `app/data.py` and includes:

- A three-machine equipment catalogue.
- Manual excerpts for troubleshooting and calibration.
- Maintenance log records tied to the equipment IDs.
- Safety procedure steps and PPE requirements.

These records are intentionally static and in-memory for the frontend prototype.

## Test

From the repository root:

```bash
pytest -q backend/tests/test_schemas.py
```

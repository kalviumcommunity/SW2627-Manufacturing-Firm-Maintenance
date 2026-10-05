# Manufacturing Floor Assistant

A tool that gives floor technicians immediate, source-referenced fixes during machine failures — pulling from equipment manuals, maintenance logs, and safety procedures — to cut downtime.

## Problem

Technicians on the floor need fast answers when equipment fails, but the knowledge to fix it is scattered across manuals, historical maintenance logs, and safety documents. Digging through these manually during a failure event slows everything down. This project aims to surface the right fix, with its source, in the moment it's needed.

## Tech Stack

- **Frontend:** Next.js (React + TypeScript)
- **Backend:** FastAPI (Python)

## Repo Structure

```
.
├── frontend/       # Next.js (TypeScript) app
├── backend/        # FastAPI app
│   ├── app/
│   │   ├── main.py
│   │   ├── schemas.py
│   │   └── __init__.py
│   ├── tests/
│   │   └── test_schemas.py
│   ├── README.md
│   └── requirements.txt
├── daily-updates/
│   └── README-2026-09-21.md
└── README.md
```

## Weekly Backend Plan

- **Day 1 (Mon):** API scaffold, simulated data model, and base endpoints
- **Day 2 (Tue):** Define typed domain and API contract
- **Day 3 (Wed):** Add fictional equipment catalogue and source records
- **Day 4 (Thu):** Improve matching logic and retrieval ranking for troubleshooting responses
- **Day 5 (Fri):** Expose search and assistant APIs with validated request/response flows
- **Day 6 (Sat):** Testing pass, cleanup, and API docs review
- **Day 7 (Sun):** Final demo prep and PR consolidation

## Getting Started

### Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Backend API Endpoints

- `GET /health` - initial service health check
- `POST /api/v1/search` - ranked source search with optional equipment and document-type filters
- `POST /api/v1/assistant` - source-referenced troubleshooting guidance

Day 2 contract models are defined in [backend/app/schemas.py](backend/app/schemas.py). They cover equipment, manuals, maintenance logs, safety procedures, search, assistant responses, source excerpts, and errors.

### Frontend (Next.js)

```bash
cd frontend
npm install
npm run dev
```

## Status

- Day 1 backend scaffold is complete.
- Day 2 schemas and API contract are complete.
- Day 3 seed data layer is in place with fictional equipment, manuals, maintenance logs, and safety procedures.
- Day 4 retrieval logic is active with source ranking and assistant response generation.
- Day 5 search and assistant API routes are available under `/api/v1`.
- Day 6 edge-case tests and OpenAPI route metadata are complete.
- Frontend integration and broader tests are planned for later days.

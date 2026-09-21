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
│   │   ├── data.py
│   │   ├── main.py
│   │   ├── schemas.py
│   │   └── services.py
│   ├── tests/
│   │   └── test_api.py
│   ├── README.md
│   └── requirements.txt
├── daily-updates/
│   └── README-2026-09-21.md
└── README.md
```

## Weekly Backend Plan

- **Day 1 (Mon):** API scaffold, simulated data model, and base endpoints
- **Day 2 (Tue):** Add issue-guidance endpoint with source references
- **Day 3 (Wed):** Integrate frontend with machine and guidance APIs
- **Day 4 (Thu):** Improve matching logic and response contracts
- **Day 5 (Fri):** Add auth/role scaffolding (if required), tighten validations
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

- `GET /api/v1/health` - service health check and version
- `GET /api/v1/equipment` - list available equipment
- `GET /api/v1/equipment/{equipment_id}` - equipment context and source inventory
- `GET /api/v1/search?q=...` - ranked source excerpts with optional filters
- `POST /api/v1/assistant/query` - deterministic source-referenced troubleshooting response

The original `/health`, `/machines`, and `/guidance` endpoints remain available for compatibility. See [backend/README.md](backend/README.md) for request examples and testing instructions.

### Frontend (Next.js)

```bash
cd frontend
npm install
npm run dev
```

## Status

- Backend v0.1 implementation includes simulated equipment data, ranked source search, safety-first assistant responses, CORS, and automated API tests.
- Frontend integration pending.

# Manufacturing Floor Assistant

A tool that gives floor technicians immediate, source-referenced fixes during machine failures, drawing on equipment manuals, maintenance logs, and safety procedures to help reduce downtime.

## Problem

Technicians on the floor need fast answers when equipment fails, but useful knowledge is scattered across manuals, historical maintenance logs, and safety documents. This project aims to surface relevant fixes and their sources when they are needed.

## Tech Stack

- **Frontend:** Next.js (React and JavaScript)
- **Backend:** FastAPI (Python)

## Repository Structure

```
.
├── app/            # Next.js App Router pages and styles
├── components/     # Shared frontend components
├── lib/            # Frontend mock data
├── backend/        # FastAPI service and tests
└── package.json    # Frontend scripts and dependencies
```

## Getting Started

### Frontend (Next.js)

Requires Node.js 18.17 or later.

```bash
npm install
npm run dev
```

Open http://localhost:3000.

Technician flow: Login -> Dashboard -> Chat -> Answer Detail -> Dashboard; Dashboard -> Machine History.

Admin flow: Login (Admin toggle) -> Admin Dashboard -> Documents -> Analytics.

The current frontend uses mock data in `lib/data.js`.

### Backend (FastAPI)

```bash
cd backend
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend API endpoints:

- `GET /health` - service health check
- `POST /api/v1/search` - ranked source search with optional equipment and document-type filters
- `POST /api/v1/assistant` - source-referenced troubleshooting guidance

## Weekly Backend Plan

- **Day 1 (Mon):** API scaffold, simulated data model, and base endpoints
- **Day 2 (Tue):** Define typed domain and API contract
- **Day 3 (Wed):** Add fictional equipment catalogue and source records
- **Day 4 (Thu):** Improve matching logic and retrieval ranking for troubleshooting responses
- **Day 5 (Fri):** Expose search and assistant APIs with validated request/response flows
- **Day 6 (Sat):** Testing pass, cleanup, and API docs review
- **Day 7 (Sun):** Final demo prep and PR consolidation

## Status

- Backend API, domain schemas, seed data, retrieval logic, and OpenAPI route metadata are implemented.
- Backend tests are in `backend/tests/`.
- The frontend technician and admin flows are implemented with mock data.

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
├── backend/        # FastAPI app
│   ├── app/
│   │   ├── main.py
│   │   ├── data.py
│   │   ├── services.py
│   │   ├── schemas.py
│   │   └── __init__.py
│   ├── tests/
│   │   │   ├── test_api.py
│   │   │   ├── test_data.py
│   │   │   ├── test_schemas.py
│   │   │   └── test_services.py
│   ├── README.md
│   └── requirements.txt
├── daily-updates/  # Local, git-ignored daily implementation notes
├── PR_README.md    # Local, git-ignored cumulative PR summary
├── pytest.ini
└── README.md
```

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

- `GET /health` - initial service health check
- `GET /api/v1/equipment` - equipment catalogue for frontend machine selection
- `POST /api/v1/search` - ranked source search with optional equipment and document-type filters
- `POST /api/v1/assistant` - source-referenced troubleshooting guidance

### Frontend integration

The backend is ready for a frontend running on `http://localhost:3000` or `http://127.0.0.1:3000`. Use `GET /api/v1/equipment` to populate machine selection, then send the selected equipment ID to the search and assistant endpoints.

## Status

- Day 1 backend scaffold is complete.
- Day 2 schemas and API contract are complete.
- Day 3 seed data layer is in place with fictional equipment, manuals, maintenance logs, and safety procedures.
- Day 4 retrieval logic is active with source ranking and assistant response generation.
- Day 5 search and assistant API routes are available under `/api/v1`.
- Day 6 edge-case tests and OpenAPI route metadata are complete.
- Day 7 frontend integration surface and final validation are complete.

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
└── README.md
```

*(Structure will evolve as each side gets set up — placeholders for now.)*

## Getting Started

### Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend (Next.js)

```bash
cd frontend
npm install
npm run dev
```

## Status

Early setup — architecture and API contracts to be defined.

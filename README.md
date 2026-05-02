# CarBuilder MVP

Monorepo with:
- `backend/` FastAPI + SQLite seed data for BMW E90 328i (N52, 2006-2011)
- `frontend/` Next.js UI with car selector, categories, parts grid, and build-list sidebar

## Run backend
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Run frontend
```bash
cd frontend
npm install
npm run dev
```

Set `NEXT_PUBLIC_API_BASE_URL` if backend is not at `http://127.0.0.1:8000`.

# AI Summarizer

A full-stack coding challenge project built with **FastAPI** (backend) and **React** (frontend).
This app lets users paste text, generate AI-powered summaries (via OpenAI API), and manage them with search, filters, and export options.

---

## Features

* **Text Summarization** using OpenAI API with three styles:

  * Concise
  * Detailed
  * Bullet points
* **Persistent Storage** with SQLite (easily swappable to Postgres/MySQL).
* **History of Summaries** – browse past results in a clean card-based layout.
* **Search & Filter** – query summaries by keyword or style.
* **Export Options**

  * Export individual summaries → **Markdown** or **PDF**
  * Export all summaries → **Markdown** or **Plain Text**
* **Rate Limiting** – simple guard (3 requests/min per IP) to prevent abuse.
* **Error Handling** – user-friendly messages if OpenAI requests fail.
* **Developer Experience**

  * Modular backend (services, schemas, crud, api routers).
  * Clear frontend structure (React components with separation of concerns).
  * Git-ready with `.gitignore` for backend + frontend.

---

## Project Structure

```
summarizer/
│
├── backend/                # FastAPI backend
│   ├── app/
│   │   ├── api/            # Routes & dependencies
│   │   ├── crud.py         # DB CRUD logic
│   │   ├── models.py       # SQLAlchemy models
│   │   ├── schemas.py      # Pydantic schemas
│   │   ├── services/       # Summarizer + OpenAI client
│   │   ├── main.py         # FastAPI app entrypoint
│   │   └── config.py       # Settings (env vars)
│   ├── .env                # OPENAI_API_KEY, DATABASE_URL
│   └── requirements.txt
│
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # SummaryForm, SearchBar, SummaryList
│   │   ├── api.js          # Axios API client
│   │   ├── App.jsx         # Main app
│   │   └── App.css         # Styling
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## 🛠 Setup & Running

### 1. Backend

#### Requirements

* Python 3.10+
* Virtual environment (`venv` or `conda`)

#### Install

```bash
cd backend
python -m venv venv
source venv/bin/activate   # (or venv\Scripts\activate on Windows)
pip install -r requirements.txt
```

#### Configure

Create `.env` in `backend/`:

```
OPENAI_API_KEY=sk-yourkeyhere
DATABASE_URL=sqlite:///./summaries.db
```

#### Run

```bash
uvicorn app.main:app --reload
```

Backend runs at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

### 2. Frontend

#### Requirements

* Node.js 18+

#### Install

```bash
cd frontend
npm install
```

#### Run

```bash
npm run dev
```

Frontend runs at: **[http://localhost:5173](http://localhost:5173)**

---

## Example API Calls

### Health check

```bash
curl http://127.0.0.1:8000/api/health
```

### Create summary

```bash
curl -X POST http://127.0.0.1:8000/api/summaries \
  -H "Content-Type: application/json" \
  -d '{"text": "FastAPI is a modern Python web framework.", "style": "concise"}'
```

---

## Environment Variables

| Variable       | Example                    | Description             |
| -------------- | -------------------------- | ----------------------- |
| OPENAI_API_KEY | `sk-proj-xxxx`             | Your OpenAI API key     |
| DATABASE_URL   | `sqlite:///./summaries.db` | Database connection URL |

---

## Bonus Points Implemented

* Adjustable summary style (concise/detailed/bullets)
* Basic rate limiting guard
* Search/filter on saved summaries
* Export options (Markdown, PDF, Text)
* Modular code structure (services, crud, schemas, components)
* Documentation (`README.md`)

---

## Deployment Notes

* **Backend**: Containerize with Docker (`FROM python:3.11-slim`, copy app, install reqs, expose 8000).
* **Frontend**: Build with `npm run build`, serve `/dist` via Netlify/Vercel or Nginx.
* **Database**: Swap SQLite with PostgreSQL by updating `DATABASE_URL`.

---

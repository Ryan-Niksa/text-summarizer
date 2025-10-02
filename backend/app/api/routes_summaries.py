from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from ..schemas import SummarizeIn, SummaryOut, ListOut
from ..crud import create_summary, list_summaries
from ..services import summarizer
from .deps import get_db

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok", "service": "summarizer-api"}

@router.get("/summaries", response_model=ListOut)
def get_summaries(
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    items, total = list_summaries(db, limit=limit, offset=offset)
    return {"items": items, "total": total}

@router.post("/summaries", response_model=SummaryOut)
def create_summary_from_text(payload: SummarizeIn, db: Session = Depends(get_db)):
    """
    Stage 1: use local heuristic for immediate usability.
    Stage 2: swap to OpenAI (same interface).
    """
    s = summarizer.summarize(payload.text, style=payload.style)
    row = create_summary(db, original_text=payload.text, summary=s, style=payload.style)
    return row

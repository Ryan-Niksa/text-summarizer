from fastapi import APIRouter, Depends, Query, Request
from sqlalchemy.orm import Session
from ..schemas import SummarizeIn, SummaryOut, ListOut
from ..crud import create_summary, list_summaries
from ..services import summarizer
from .deps import get_db
from .rate_limit import check_rate_limit

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok", "service": "summarizer-api"}

@router.get("/summaries", response_model=ListOut)
def get_summaries(
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    q: str | None = Query(None),
    style: str | None = Query(None),
    db: Session = Depends(get_db),
):
    items, total = list_summaries(db, q=q, style=style, limit=limit, offset=offset)
    return {"items": items, "total": total}

@router.post("/summaries", response_model=SummaryOut)
def create_summary_from_text(
    payload: SummarizeIn,
    request: Request,
    db: Session = Depends(get_db)
):

    check_rate_limit(request)

    s = summarizer.summarize(payload.text, style=payload.style)
    row = create_summary(db, original_text=payload.text, summary=s, style=payload.style)
    return row

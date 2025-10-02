from sqlalchemy.orm import Session
from sqlalchemy import select, func
from . import models

def create_summary(db: Session, *, original_text: str, summary: str, style: str) -> models.Summary:
    row = models.Summary(original_text=original_text, summary=summary, style=style)
    db.add(row)
    db.commit()
    db.refresh(row)
    return row

def list_summaries(
    db: Session,
    *,
    q: str | None = None,
    style: str | None = None,
    limit: int = 50,
    offset: int = 0
):
    stmt = select(models.Summary).order_by(models.Summary.id.desc())

    if q:
        like = f"%{q}%"
        stmt = stmt.where(
            (models.Summary.original_text.ilike(like)) |
            (models.Summary.summary.ilike(like))
        )
    if style:
        stmt = stmt.where(models.Summary.style == style)

    total = db.execute(
        select(func.count()).select_from(stmt.subquery())
    ).scalar_one()

    items = db.execute(stmt.offset(offset).limit(limit)).scalars().all()
    return items, total

from sqlalchemy.orm import Session
from sqlalchemy import select, func
from . import models

def create_summary(db: Session, *, original_text: str, summary: str, style: str) -> models.Summary:
    row = models.Summary(original_text=original_text, summary=summary, style=style)
    db.add(row)
    db.commit()
    db.refresh(row)
    return row

def list_summaries(db: Session, *, limit: int = 50, offset: int = 0):
    total = db.execute(select(func.count(models.Summary.id))).scalar_one()
    items = db.execute(
        select(models.Summary)
        .order_by(models.Summary.id.desc())
        .offset(offset)
        .limit(limit)
    ).scalars().all()
    return items, total

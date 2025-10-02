from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, String, DateTime, func, Integer
from .db import Base

class Summary(Base):
    __tablename__ = "summaries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    original_text: Mapped[str] = mapped_column(Text, nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    style: Mapped[str] = mapped_column(String(20), default="concise", nullable=False)
    created_at: Mapped[str] = mapped_column(DateTime(timezone=True),
        server_default=func.now(),
        nullable=False)

from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime

SummaryStyle = Literal["concise", "detailed", "bullets"]

class SummarizeIn(BaseModel):
    text: str = Field(..., min_length=1, description="Raw input text to summarize")
    style: SummaryStyle = "concise"

class SummaryOut(BaseModel):
    id: int
    summary: str
    style: str
    created_at: datetime

    class Config:
        from_attributes = True

class SummaryRow(BaseModel):
    id: int
    original_text: str
    summary: str
    style: str
    created_at: datetime

    class Config:
        from_attributes = True

class ListOut(BaseModel):
    items: list[SummaryRow]
    total: int

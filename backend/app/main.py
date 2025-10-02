from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import Base, engine
from .api.routes_summaries import router as summaries_router
from .config import settings

app = FastAPI(title="AI Summarizer API", version="0.1.0")

# Create tables on startup (simple for the challenge)
@app.on_event("startup")
def startup() -> None:
    Base.metadata.create_all(bind=engine)

origins = settings.FRONTEND_ORIGINS or ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(summaries_router, prefix="/api")

from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.routers import courses
from src.database import engine, Base, SessionLocal
from src.seed import seed_db

# Create DB tables
Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Seed the database on startup so Scheduler API has data to work with
    db = SessionLocal()
    try:
        seed_db(db)
    finally:
        db.close()
    yield

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Course API",
    version="1.0.0",
    description="Manages course catalog and metadata.",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(courses.router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "ok"}

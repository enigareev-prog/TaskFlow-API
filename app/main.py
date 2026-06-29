from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.tasks import router as tasks_router

app = FastAPI(
    title="TaskFlow API",
    description="Backend API for tasks, projects and learning progress",
    version="0.1.0",
)

app.include_router(health_router)
app.include_router(tasks_router)
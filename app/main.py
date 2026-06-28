from fastapi import FastAPI

app = FastAPI(
    title="TaskFlow API",
    description="Backend API for tasks, projects and learning progress",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "taskflow-api",
        "version": "0.1.0",
    }
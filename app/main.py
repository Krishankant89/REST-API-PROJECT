from fastapi import FastAPI

from app.database import Base, engine
from app.routes.tasks import router as task_router

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Task Management API",
    version="1.0.0"
)

# Register routes
app.include_router(task_router)


@app.get("/")
def root():
    return {
        "message": "FastAPI Task Management API is running"
    }
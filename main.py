from fastapi import FastAPI
from task_routes import router as task_router
from database import Base, engine
from middleware.auth import AuthMiddleware 

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Service",
    description="Task microservice to manage user tasks.",
    version="1.0.0"
)
app.add_middleware(AuthMiddleware)
app.include_router(task_router)


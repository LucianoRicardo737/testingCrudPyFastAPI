from fastapi import FastAPI
from src.routes.user import user

app = FastAPI(
    title="TestingPy",
    description="Testing python crud",
    version="0.1",
    openapi_tags=[{
        "name":"users",
        "description": "User routes"
    }]
)

app.include_router(user)
from fastapi import FastAPI

from api.v1.api_router import api_router
from core.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(api_router)


@app.get("/")
async def root():
    return {
        "message": "Hello World",
        "status": "success",
        "apiVersion": {
            "v1": {
                "employee": "/employee",
            }
        },
    }


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

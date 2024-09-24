# main.py
from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from app.controllers import routers

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up the API...")
    yield
    print("Shutting down the API...")

app = FastAPI(lifespan=lifespan)

for router in routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

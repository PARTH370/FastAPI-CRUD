import os
import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from app.user_registration.views import router as user_router


app = FastAPI(title="Testing", version="0.1.0")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/user")

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")

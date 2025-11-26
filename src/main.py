from fastapi import FastAPI
from routers.base_router import base_router


# Create instance of FastAPI
app = FastAPI()


# Include base router
app.include_router(base_router)

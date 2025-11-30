from fastapi import FastAPI
from routers import base_router, data_router

# Create instance of FastAPI
app = FastAPI()


# Include routers
app.include_router(base_router)
app.include_router(data_router)

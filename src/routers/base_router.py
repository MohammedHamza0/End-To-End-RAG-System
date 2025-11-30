from fastapi import APIRouter, Depends
from helpers.config import Settings, get_settings


# Create instance of APIRouter
base_router = APIRouter(prefix="/Base", tags=["Base"])

@base_router.get(path="/welcome", description="EndPoint for Healthy-Check")
async def welcome(settings: Settings = Depends(get_settings)):
    APP_NAME = settings.APP_NAME
    VERSION = settings.VERSION
    return {
        "message":"Welcome to the End-to-End RAG System",
        "app_name": APP_NAME,
        "version": VERSION
        }


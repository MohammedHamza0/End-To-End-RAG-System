from fastapi import APIRouter



# Create instance of APIRouter
base_router = APIRouter(prefix="/Base", tags=["Base"])

@base_router.get(path="/welcome", description="EndPoint for Healthy-Check")
async def welcome():
    return {
        "message":"Welcome to the End-to-End RAG System"
        }


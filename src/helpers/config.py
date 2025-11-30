from pydantic_settings import BaseSettings
from typing import List
from functools import lru_cache


# Class for validate variables configuration
class Settings(BaseSettings):
     class Config:
          env_file = ".env"
     
     APP_NAME: str
     VERSION: str
     OPENAI_API_KEY: str
     GEMINI_API_KEY: str
     FILE_ALLOWED_EXTENSIONS: List[str]
     FILE_MAX_SIZE: int
     FILE_DEFUALT_CHUNK_SIZE: int
     


# Function to get settings instance
@lru_cache(maxsize=1, typed=False)
def get_settings() -> Settings:
     return Settings()
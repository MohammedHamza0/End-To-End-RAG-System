from fastapi import Depends, UploadFile, HTTPException, status
import os
from fastapi.responses import JSONResponse
from helpers.config import Settings, get_settings

class BaseController:
     def __init__(self, settings: Settings = Depends(get_settings)):
          self.settings = settings
          self.project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
          self.files_dir = os.path.join(self.project_dir, "assets", "files")
          self.openai_api_key = settings.OPENAI_API_KEY
          self.gemini_api_key = settings.GEMINI_API_KEY
          self.file_allowed_extensions = settings.FILE_ALLOWED_EXTENSIONS
          self.file_max_size = settings.FILE_MAX_SIZE
     
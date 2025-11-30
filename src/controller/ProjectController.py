from fastapi import Depends, File, UploadFile, status
from fastapi.responses import JSONResponse
import os
import aiofiles
import random
import string
import logging
logger = logging.getLogger("uvicorn.error")
from helpers.config import Settings, get_settings
from .BaseController import BaseController
from .DataController import DataController
from models import ResponseEnum





# Class to work with project files and directories
class ProjectController(BaseController):
     def __init__(self, settings: Settings = Depends(get_settings)):
          super().__init__(settings)
          
     # Function to create project files directory and return the full path
     def get_project_files_dir(self, project_id: str):
          full_files_path = os.path.join(self.files_dir, project_id)
          os.makedirs(full_files_path, exist_ok=True)
          return full_files_path
     
     # Function to save uploaded file
     async def files_save(self, project_id: str, file: UploadFile = File(...),
                          new_file_name:str = "".join(random.choices(string.ascii_letters + string.digits, k=12))) -> str:
          
          files_save_path = self.get_project_files_dir(project_id=project_id)
          file_path = os.path.join(files_save_path, new_file_name)
          try:
               async with aiofiles.open(file_path, mode='wb') as f:
                    while chunk := await file.read(size=self.settings.FILE_DEFUALT_CHUNK_SIZE):
                         await f.write(chunk)
          except Exception as e:
               logger.error(f"Error saving file: {e}")
               return JSONResponse(
                    content={
                         "message": ResponseEnum.FILE_UPLOADED_FAILED.value 
                    },
                    status_code= status.HTTP_500_INTERNAL_SERVER_ERROR
               )
          return file_path



     
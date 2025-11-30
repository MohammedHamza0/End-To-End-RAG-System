from fastapi import Depends, UploadFile, HTTPException, status
import string
import random
from fastapi.responses import JSONResponse
from helpers.config import Settings, get_settings
from .BaseController import BaseController
from models import ResponseEnum



# Class for data controller extends BaseController to validate data 
class DataController(BaseController):
     def __init__(self, settings: Settings = Depends(get_settings)):
          super().__init__(settings)
          self.settings = settings

     # Function for file validation
     def validate_uploaded_file(self, file: UploadFile) -> (JSONResponse, bool):

          # Validate file type
          if file.content_type not in self.file_allowed_extensions:
               return JSONResponse(
                    content= {
                         "message": ResponseEnum.FILE_TYPE_NOT_SUPPORTED.value,
                         "allowed_extensions": self.file_allowed_extensions,
                         "file_type": file.content_type
                    },
                    status_code=status.HTTP_400_BAD_REQUEST
               ), False

          # Validate file size
          elif file.size > self.file_max_size:
               return JSONResponse(
                    content= {
                         "message": ResponseEnum.FILE_SIZE_TOO_LARGE.value,
                         "max_file_size": self.file_max_size,
                         "file_size": file.size
                    },
                    status_code=status.HTTP_400_BAD_REQUEST
               ), False
          
          # If file is valid
          else:
               return JSONResponse(
                    content= {
                         "message": ResponseEnum.FILE_UPLOADED_SUCCESSFULLY.value,
                         "file_name": file.filename,
                         "file_type": file.content_type,
                         "file_size": file.size
                    },
                    status_code=status.HTTP_200_OK
               ), True
          

     # Function for generating unique file name
     def generate_unique_clean_file_name(self, file_name: str, length: int = 12) -> str:
          generated_prefix_file_name = "".join(random.choices(string.ascii_letters + string.digits, k=length))
          new_unique_file_name = f"{generated_prefix_file_name}_{file_name}"
          new_unique_file_name = new_unique_file_name.replace(" ", "_")
          return new_unique_file_name

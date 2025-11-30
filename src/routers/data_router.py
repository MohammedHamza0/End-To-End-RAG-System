from fastapi import APIRouter, Depends, File, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import Settings, get_settings
from controller import DataController, ProjectController
from models import ResponseEnum


# Create instance for data router
data_router = APIRouter(prefix="/Data", tags=["Data"])

# Function to upload file 
@data_router.post(path="/upload_file/{project_id}", 
                  description="EndPoint for uploading file under a specific project id")
async def upload_file(project_id: str, 
                         settings: Settings = Depends(get_settings), 
                         file: UploadFile = File(...)):
          
          # Create instance for data controller
          data_controller = DataController(settings)
          # validate uploaded file
          message, status = data_controller.validate_uploaded_file(file)
          if status:
               project_controller = ProjectController(settings)
               # generate unique clean file name
               new_file_name = data_controller.generate_unique_clean_file_name(file.filename)
               # save the uploaded file under the project id
               file_path = await project_controller.files_save(project_id, file, new_file_name)
               return JSONResponse(
                    content={
                         "message": ResponseEnum.FILE_UPLOADED_SUCCESSFULLY.value, 
                         "file_name": new_file_name,
                         "file_size": (file.size) / (1024 * 1024) + "MB",
                         "file_type": file.content_type,
                         "file_path": file_path,
                         "project_id": project_id,

                         }
               )
          return message

               
               
    
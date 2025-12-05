from fastapi import APIRouter, Depends, File, UploadFile, status
import json
from fastapi.responses import JSONResponse
from helpers.config import Settings, get_settings
from controller import DataController, ProjectController, ProcessController
from models import ResponseEnum
from .schemas.data import ProcessRequest


# Create instance for data router
data_router = APIRouter(prefix="/Data", tags=["Data"])

# EndPoint for uploading file 
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
               new_file_name, file_path = data_controller.generate_unique_clean_file_name(project_id=project_id, file_name=file.filename)
               # save the uploaded file under the project id
               file_path = await project_controller.files_save(project_id, file, new_file_name)
               return JSONResponse(
                    content={
                         "message": ResponseEnum.FILE_UPLOADED_SUCCESSFULLY.value, 
                         "file_name": new_file_name,
                         "file_size": "{:.2f} MB".format(file.size / (1024 * 1024)),
                         "file_type": file.content_type,
                         "file_path": file_path,  
                         "project_id": project_id,

                         }
               )
          return message




# Endpoint for processing file under a specific project id
@data_router.post(path="/process/{project_id}", description="EndPoint for processing file under a specific project id")
async def process_file(project_id: str, process_request: ProcessRequest,
                       process_controller: ProcessController = Depends(ProcessController)):
     file_id = process_request.file_id
     chunk_size = process_request.chunk_size
     chunk_overlap = process_request.chunk_overlap

     # Extract file content
     file_content = process_controller.get_file_content(file_id=file_id)
     if file_content != None:
          chunks = process_controller.process_file_content(file_content=file_content, 
                                                            file_id=file_id,
                                                            chunk_size=chunk_size,
                                                            overlap_size=chunk_overlap)
          return JSONResponse(
               content={
                    "message": ResponseEnum.FILE_PROCESSED_SUCCESSFULLY.value,
               },
               status_code=status.HTTP_200_OK
          ), chunks
     
     return JSONResponse(
          content={
               "message": ResponseEnum.FILE_PROCESSED_FAILED.value
          },
          status_code=status.HTTP_400_BAD_REQUEST
     )

               
               
    
from enum import Enum




class ResponseEnum(Enum):
     FILE_UPLOADED_SUCCESSFULLY = "File uploaded successfully"
     FILE_TYPE_NOT_SUPPORTED = "File type not supported"
     FILE_SIZE_TOO_LARGE = "File size too large"
     FILE_UPLOADED_FAILED = "File uploaded failed"
     FILE_PROCESSED_SUCCESSFULLY = "File processed successfully"
     FILE_PROCESSED_FAILED = "File processed failed"
     
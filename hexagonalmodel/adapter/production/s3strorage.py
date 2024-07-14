from typing import Any
from hexagonalmodel.domain.base import settings
from hexagonalmodel.port.storage import StoragePort
import boto3

EXTENSION_ALLOWED_LIST = ['png','jpg','jpeg']

class S3StorageAdapter(StoragePort):
    
    def __init__(self) -> None:
        self.s3 = boto3.client('s3')
        
    def upload_employee_image_file(self, image: Any, employee_id: int) -> str:
        extension = image.filename.split('.')[-1]
        if extension in EXTENSION_ALLOWED_LIST:
            
            file_name = f'employee-image-{employee_id}.{extension}'
            self.s3.upload_fileobj(
                image,
                settings.BUCKET_NAME,
                file_name,
                ExtraArgs={
                    'ACL':'public-read',
                    'ContentType':image.content_type
                }
            )
            
            image_path = f'{settings.BUCKET_URL}/{file_name}'
            
            return image_path
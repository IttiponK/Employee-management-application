import base64
from typing import Any
from hexagonalmodel.domain.base import settings
from hexagonalmodel.port.storage import StoragePort
import boto3


class S3StorageAdapter(StoragePort):
    
    def __init__(self) -> None:
        self.s3 = boto3.resource(
            's3',
        )
        
    def upload_employee_image_file(self, image: Any, employee_id: int) -> str:
        
        file_name = f'employee-image-{employee_id}'
        extension = 'jpg'
                    
        full_file_name = f'{file_name}.{extension}'
        self.s3.Object(settings.BUCKET_NAME,full_file_name).put(Body=base64.b64decode(image),ACL='public-read')
        image_path = f'{settings.BUCKET_URL}/{full_file_name}'
        
        return image_path
        
        

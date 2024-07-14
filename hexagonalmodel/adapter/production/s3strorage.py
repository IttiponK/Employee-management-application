from hexagonalmodel.domain.base import settings
from hexagonalmodel.port.storage import StoragePort
import boto3

class S3StorageAdapter(StoragePort):
    
    def __init__(self) -> None:
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
        
    def upload_employee_image_file(self, image: bytes) -> str:
        self.s3.upload_fileobj(
            image,
            'test',
            'test',
            ExtraArgs={
                'ACL':'public-read',
                'ContentType':''
            }
        )
        
        return 'test'
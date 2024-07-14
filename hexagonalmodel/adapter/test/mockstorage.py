from typing import Any
from hexagonalmodel.port.storage import StoragePort

class MockStorage(StoragePort):
    
    def upload_employee_image_file(self, image: Any, employee_id: int) -> str:
        pass 
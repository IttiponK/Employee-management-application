from hexagonalmodel.port.storage import StoragePort

class MockStorage(StoragePort):
    
    def upload_employee_image_file(self, image: bytes) -> None:
        pass 
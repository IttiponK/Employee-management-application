from abc import ABC,abstractmethod

class StoragePort(ABC):
    
    @abstractmethod
    def upload_employee_image_file(self,image: bytes) -> str:
        """ upload employee image to storage 

        Args:
            image (bytes): image byte

        Returns:
            str: image path
        """             
        
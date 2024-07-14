from abc import ABC,abstractmethod
from typing import Any

class StoragePort(ABC):
    
    @abstractmethod
    def upload_employee_image_file(self,image: Any,employee_id:int) -> str:
        """ upload employee image to storage 

        Args:
            image (Any): image object
            employee_id (int): employee id

        Returns:
            str: image path
        """             
        
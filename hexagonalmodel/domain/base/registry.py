from hexagonalmodel.domain.base.singleton import Singleton
from typing import Optional

class Registry(metaclass=Singleton):
    
    def __init__(self) -> None:
        
        from hexagonalmodel.port.encryption import EncryptionPort
        self.encryption:Optional[EncryptionPort] = None 
        
        from hexagonalmodel.port.db import DbPort
        self.db:Optional[DbPort] = None
        
        from hexagonalmodel.port.storage import StoragePort
        self.storage:Optional[StoragePort] = None
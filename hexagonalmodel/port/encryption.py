from abc import ABC,abstractmethod 

class EncryptionPort(ABC):
    
    
    @abstractmethod
    def verify_plaintext(self,plaintext: str, encrypt: str) -> None:
        """ verify plain text and encrypt text are the same

        Args:
            plaintext (str): plain text that not encrypt
            encrypt (str): encrypt text 
        """        
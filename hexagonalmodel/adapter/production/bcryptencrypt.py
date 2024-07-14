import bcrypt
from hexagonalmodel.domain.base import exception
from hexagonalmodel.port.encryption import EncryptionPort


class BcryptEncryptionAdapter(EncryptionPort):
    
    def verify_plaintext(self, plaintext: str, encrypt: str) -> None:
 
        if not bcrypt.checkpw(bytes(plaintext.encode()),bytes(encrypt.encode())):
            raise exception.InvalidAuthorize
        
        
if __name__ == '__main__':
    
    plaintext = ''
    encrypt = ''
    adapter = BcryptEncryptionAdapter().verify_plaintext(plaintext,encrypt)
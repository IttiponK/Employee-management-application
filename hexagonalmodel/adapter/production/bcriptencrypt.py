from hexagonalmodel.port.encryption import EncryptionPort

class BcryptEncryptAdapter(EncryptionPort):
    
    def verify_plaintext(self, plaintext: str, encrypt: str) -> None:
        return super().verify_plaintext(plaintext, encrypt)
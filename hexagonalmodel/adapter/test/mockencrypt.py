from hexagonalmodel.port.encryption import EncryptionPort

class MockEncrypt(EncryptionPort):
    
    def verify_plaintext(self, plaintext: str, encrypt: str) -> None:
        pass 
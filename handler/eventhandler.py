from hexagonalmodel.domain.base.registry import Registry

def dependency_injection():
    
    from hexagonalmodel.adapter.production.mariadb import MariaDbAdapter
    Registry().db = MariaDbAdapter()
    
    from hexagonalmodel.adapter.production.bcryptencrypt import BcryptEncryptionAdapter
    Registry().encryption = BcryptEncryptionAdapter()
    
    from hexagonalmodel.adapter.production.s3strorage import S3StorageAdapter
    Registry().storage = S3StorageAdapter()
    

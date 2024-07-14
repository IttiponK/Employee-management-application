class InvalidAuthorize(Exception):
    pass 

class DbAdapterHaveSomethingWrong(Exception):
    pass 

class EncryptionAdapterHaveSomethingWrong(Exception):
    pass 

class InvalidStatusId(Exception):
    pass 

class StorageAdapterHaveSomethingWrong(Exception):
    pass 

class InvalidEmployeeId(Exception):
    pass 

class DuplicatePosition(Exception):
    pass 

class InvalidPositionId(Exception):
    pass 

class ThisPositionAlreadyUse(Exception):
    pass 

class InvalidDepartmentId(Exception):
    pass 

class ThisDepartmentAlreadyUse(Exception):
    pass 

class ThisStatusAlreadyUse(Exception):
    pass 
from pydantic import BaseModel
from hexagonalmodel.domain.model.status import StatusModel

class EmployeeModel(BaseModel):
    first_name:str 
    last_name:str 
    address:str 
    manager:bool
    status:StatusModel 
    image:str
    
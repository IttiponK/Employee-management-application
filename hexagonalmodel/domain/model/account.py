from pydantic import BaseModel
from hexagonalmodel.domain.model.employee import EmployeeModel

class AccountModel(BaseModel):
    
    username:str 
    password:str 
    owner:EmployeeModel
    deactivate:bool
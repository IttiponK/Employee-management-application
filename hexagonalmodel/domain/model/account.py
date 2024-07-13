from pydantic import BaseModel,ConfigDict
from hexagonalmodel.domain.model.employee import EmployeeModel

class AccountModel(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    username:str 
    password:str 
    owner:EmployeeModel
    deactivate:bool
from typing import Optional
from pydantic import BaseModel,ConfigDict
from hexagonalmodel.domain.model.employee import EmployeeModel

class AccountModel(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid',
        from_attributes=True
    )
    id:Optional[int] = None
    username:str 
    password:str 
    employee_owner_id:int
    deactivate:bool
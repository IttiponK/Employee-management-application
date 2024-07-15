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
    username:Optional[str] = None 
    password:Optional[str] = None 
    employee_owner_id:Optional[int] = None
    deactivate:Optional[bool] = None
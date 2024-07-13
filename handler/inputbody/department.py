from pydantic import BaseModel,ConfigDict
from typing import Optional

class CreateNewDepartment(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    department_name:str 
    manager_id:Optional[int] = None
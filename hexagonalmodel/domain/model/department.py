from pydantic import BaseModel,ConfigDict
from typing import Optional

class DepartmentModel(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    id:Optional[int] = None
    department_name:str 
    manager:Optional[int] = None
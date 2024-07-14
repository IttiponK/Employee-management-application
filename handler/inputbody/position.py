from pydantic import BaseModel,ConfigDict
from typing import Optional

class CreatePosition(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    position_name:str 
    salary:float
    department_id:int
    
class UpdataPosition(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    id:int
    position_name:Optional[str] = None
    salary:Optional[float] = None
    department_id:Optional[int] = None
    
class DeletePosition(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    id:int
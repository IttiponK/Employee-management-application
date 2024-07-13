from pydantic import BaseModel,ConfigDict
from typing import Optional

class CreatePosition(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    position_name:str 
    salary:float
    
class UpdataPosition(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    id:int
    position_name:Optional[str]
    salary:Optional[float]
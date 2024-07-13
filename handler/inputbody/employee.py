from pydantic import BaseModel,ConfigDict
from typing import Optional

class CreateNewEmployee(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    first_name:str 
    last_name:str 
    address:str 
    position_name:str 
    status:str 
    image:Optional[bytes] = None
    
class UpdateEmployee(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    id:int
    first_name:Optional[str] = None
    last_name:Optional[str] = None 
    address:Optional[str] = None 
    position_name:Optional[str] = None 
    status:Optional[str] = None 
    image:Optional[bytes] = None
    
class TerminateEmployee(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    id:int
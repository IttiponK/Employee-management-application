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
    image:Optional[bytes]
    
class UpdateEmployee(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    id:int
    first_name:Optional[str] 
    last_name:Optional[str] 
    address:Optional[str] 
    position_name:Optional[str] 
    status:Optional[str] 
    image:Optional[bytes]
    
    
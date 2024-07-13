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
    
    
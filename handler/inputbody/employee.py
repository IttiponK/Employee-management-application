from pydantic import BaseModel,ConfigDict
from typing import Any, Optional,Callable

class CreateNewEmployee(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    first_name:str 
    last_name:str 
    address:Optional[str] = None 
    position_id:int  
    status_id:int  
    department_id:int 
    image:Any = None
    
class UpdateEmployee(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    id:int
    first_name:Optional[str] = None
    last_name:Optional[str] = None 
    address:Optional[str] = None 
    position_id:Optional[int] = None 
    status_id:Optional[int] = None 
    department_id:Optional[int]
    image:Optional[bytes] = None
    
class TerminateEmployee(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    id:int
from pydantic import BaseModel,ConfigDict

class CreateNewStatus(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    status_name:str 
    
class UpdateStatus(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    id:int 
    status_name:str 
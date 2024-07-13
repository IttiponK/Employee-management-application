from pydantic import BaseModel,ConfigDict

class CreateNewStatus(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    status_name:str 
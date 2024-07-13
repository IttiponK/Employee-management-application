from pydantic import BaseModel,ConfigDict

class CreatePosition(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    position_name:str 
    salary:float
from pydantic import BaseModel,ConfigDict

class PositionModel(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    position_name:str 
    salary:float
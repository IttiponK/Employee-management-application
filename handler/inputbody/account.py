from pydantic import BaseModel,ConfigDict

class LoginModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    username:str 
    password:str 
    


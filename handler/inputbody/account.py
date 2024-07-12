from pydantic import BaseModel,Extra

class LoginModel(BaseModel):
    username:str 
    password:str 
    
    class Config:
        validate_assignment = True
        extra = 'forbid'

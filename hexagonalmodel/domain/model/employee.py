from pydantic import BaseModel,ConfigDict
from hexagonalmodel.domain.model.status import StatusModel
from hexagonalmodel.domain.model.position import PositionModel

class EmployeeModel(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    first_name:str 
    last_name:str 
    address:str 
    position:PositionModel
    status:StatusModel 
    image:str
    
    
    
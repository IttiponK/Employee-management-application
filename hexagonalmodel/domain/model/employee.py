from pydantic import BaseModel,ConfigDict
from hexagonalmodel.domain.model.status import StatusModel
from hexagonalmodel.domain.model.position import PositionModel
from hexagonalmodel.domain.model.department import DepartmentModel
from typing import Optional

class EmployeeModel(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid'
    )
    
    id:Optional[int] = None
    first_name:str 
    last_name:str 
    address:str 
    image:str
    
    position_id:int 
    status_id:int 
    department_id:int
    
    position:Optional[PositionModel] = None
    status:Optional[StatusModel] = None
    department:Optional[DepartmentModel] = None
    
    
    
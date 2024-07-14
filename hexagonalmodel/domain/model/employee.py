from pydantic import BaseModel,ConfigDict
from hexagonalmodel.domain.model.status import StatusModel
from hexagonalmodel.domain.model.position import PositionModel
from hexagonalmodel.domain.model.department import DepartmentModel
from typing import Optional

class EmployeeModel(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid',
        from_attributes=True
    )
    
    id:Optional[int] = None
    first_name:Optional[str] = None
    last_name:Optional[str] = None
    address:Optional[str] = None
    image:Optional[str] = None
    
    position_id:Optional[int] = None 
    status_id:Optional[int] = None 
    department_id:Optional[int] = None
    
    position:Optional[PositionModel] = None
    status:Optional[StatusModel] = None
    department:Optional[DepartmentModel] = None
    
    
    
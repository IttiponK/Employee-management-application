from pydantic import BaseModel,ConfigDict
from typing import Optional

class PositionModel(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid',
        from_attributes=True
    )
    
    id:Optional[int] = None
    position_name:Optional[str] = None
    salary:Optional[float] = None
    department_id:Optional[int] = None
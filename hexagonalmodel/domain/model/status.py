from pydantic import BaseModel,ConfigDict
from typing import Optional

class StatusModel(BaseModel):
    
    model_config = ConfigDict(
        validate_assignment=True,
        extra='forbid',
        from_attributes=True
    )
    
    id:Optional[int] = None
    status_name:str
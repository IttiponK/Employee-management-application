from hexagonalmodel.domain.base.registry import Registry
from handler import inputbody
from hexagonalmodel.domain.model.position import PositionModel
from typing import List

def create_new_position(input_body:inputbody.position.CreatePosition) -> int: 
    repo = Registry()
    
    new_position = PositionModel.model_validate(input_body.model_dump())
    
    id_ = repo.db.create_new_position(new_position)
    
    return id_

def get_all_position() -> List[PositionModel]:
    repo = Registry()
    
    all_position = repo.db.get_all_position()
    
    return all_position
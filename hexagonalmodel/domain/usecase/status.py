from handler import inputbody 
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.domain.model.status import StatusModel

def create_new_status(input_body:inputbody.status.CreateNewStatus) -> int: 
    repo = Registry()
    
    new_status = StatusModel.model_validate(input_body.model_dump())
    
    id_ = repo.db.create_new_status(new_status)
    
    return id_
from handler import inputbody 
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.domain.model.status import StatusModel
from typing import List

def create_new_status(input_body:inputbody.status.CreateNewStatus) -> int: 
    repo = Registry()
    
    new_status = StatusModel.model_validate(input_body.model_dump())
    
    id_ = repo.db.create_new_status(new_status)
    
    return id_

def get_all_status() -> List[StatusModel]:
    repo = Registry()
    
    all_status = repo.db.get_all_status()
    
    return all_status

def update_status(input_body: inputbody.status.UpdateStatus) -> int:
    repo = Registry()
    
    update_status_model = StatusModel.model_validate(input_body.model_dump())
    
    id_ = repo.db.update_status(update_status_model)
    
    return id_

def delete_status(input_body: inputbody.status.DeleteStatus) -> None:
    repo = Registry()
    
    repo.db.delete_status_by_id(input_body.id)
    
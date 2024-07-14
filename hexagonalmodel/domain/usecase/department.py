from handler import inputbody
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.domain.model.department import DepartmentModel
from typing import List

def create_new_department(input_body:inputbody.department.CreateNewDepartment) -> int:
    repo = Registry()
    
    new_department = DepartmentModel(
        department_name=input_body.department_name,
        manager_id=input_body.manager_id
    )
    
    id_ = repo.db.create_new_department(new_department)
    
    return id_

def get_all_department() -> List[DepartmentModel]:
    repo = Registry()
    
    all_department = repo.db.get_all_department()
    
    return all_department

def update_department(input_body: inputbody.department.UpdateDepartment) -> int:
    repo = Registry()
    
    update_department_model = DepartmentModel(
        id=input_body.id,
        department_name=input_body.department_name,
        manager_id=input_body.manager_id
    )
    
    id_ = repo.db.update_department(update_department_model)
    
    return id_

def delete_department(input_body: inputbody.department.DeleteDepartment) -> None:
    repo = Registry() 
    
    repo.db.delete_department_by_id(input_body.id)
    
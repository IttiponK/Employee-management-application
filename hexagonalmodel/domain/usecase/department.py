from handler import inputbody
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.domain.model.department import DepartmentModel

def create_new_department(input_body:inputbody.department.CreateNewDepartment) -> int:
    repo = Registry()
    
    new_department = DepartmentModel(
        department_name=input_body.department_name,
        manager=input_body.manager_id
    )
    
    id_ = repo.db.create_new_department(new_department)
    
    return id_
from hexagonalmodel.domain.base.registry import Registry
from handler import inputbody
from hexagonalmodel.domain.model.employee import EmployeeModel
from typing import List

def create_new_employee(input_body:inputbody.employee.CreateNewEmployee) -> int:
    repo = Registry()
    
    position_model = repo.db.get_position_by_position_name(position_name=input_body.position_name)
    status_model = repo.db.get_status_by_status_name(status=input_body.status)
    image_path = repo.storage.upload_employee_image_file(image=input_body.image)
    
    new_employee = EmployeeModel(
        first_name=input_body.first_name,
        last_name=input_body.last_name,
        address=input_body.address,
        position=position_model,
        status=status_model,
        image=image_path
    )
    
    id_ = repo.db.create_new_employee(new_employee)
    
    return id_
    
def get_all_employee() -> List[EmployeeModel]:
    repo = Registry()
    
    all_employee = repo.db.get_all_employee()
    
    return all_employee
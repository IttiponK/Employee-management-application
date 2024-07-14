from hexagonalmodel.domain.base.registry import Registry
from handler import inputbody
from hexagonalmodel.domain.model.employee import EmployeeModel
from typing import List

def create_new_employee(input_body:inputbody.employee.CreateNewEmployee) -> int:
    repo = Registry()
    
    repo.db.get_position_by_position_id(id_=input_body.position_id)
    repo.db.get_status_by_status_id(id_=input_body.status_id)
    repo.db.get_department_by_id(id_=input_body.department_id)
    image_path = repo.storage.upload_employee_image_file(image=input_body.image)
    
    new_employee = EmployeeModel(
        first_name=input_body.first_name,
        last_name=input_body.last_name,
        address=input_body.address,
        position_id=input_body.position_id,
        status_id=input_body.status_id,
        department_id=input_body.department_id,
        image=image_path
    )
    
    id_ = repo.db.create_new_employee(new_employee)
    
    return id_
    
def get_all_employee() -> List[EmployeeModel]:
    repo = Registry()
    
    all_employee = repo.db.get_all_employee()
    
    return all_employee

def update_employee(input_body: inputbody.employee.UpdateEmployee) -> int:
    repo = Registry()
    
        
    existing_employee_model = repo.db.get_employee_by_id(id_=input_body.id)
    
    if input_body.image:
        image_path = repo.storage.upload_employee_image_file(image=input_body.image)
    else:
        image_path = existing_employee_model.image
    
    if input_body.position_id != existing_employee_model.position_id:
        repo.db.get_position_by_position_id(id_=input_body.position_id)
        position_id = input_body.position_id
    else:
        position_id = input_body.position_id
        
    if input_body.status_id != existing_employee_model.status_id:
        repo.db.get_status_by_status_id(input_body.status_id)
        status_id = input_body.status_id
    else:
        status_id = input_body.status_id
        
    if input_body.department_id != existing_employee_model.department_id:
        repo.db.get_department_by_id(id_=input_body.department_id)
        department_id = input_body.department_id
    else:
        department_id = input_body.department_id
        
    update_employee_model = EmployeeModel(
        id=input_body.id,
        first_name=input_body.first_name,
        last_name=input_body.last_name,
        address=input_body.address,
        position_id=position_id,
        status_id=status_id,
        department_id=department_id,
        image=image_path
    )
    
    id_ = repo.db.update_employee(update_employee_model)
    
    return id_

def terminate_employee(input_body: inputbody.employee.TerminateEmployee) -> int :
    repo = Registry()
    
    existing_employee_model = repo.db.get_employee_by_id(id_=input_body.id)
    
    terminate_status = repo.db.get_status_by_status_id(status='terminate')
    
    existing_employee_model.status = terminate_status
    
    id_ = repo.db.update_employee(existing_employee_model)
    
    return id_
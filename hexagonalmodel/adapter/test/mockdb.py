from typing import List
from hexagonalmodel.domain.model.account import AccountModel
from hexagonalmodel.domain.model.department import DepartmentModel
from hexagonalmodel.domain.model.employee import EmployeeModel
from hexagonalmodel.domain.model.position import PositionModel
from hexagonalmodel.domain.model.status import StatusModel
from hexagonalmodel.port.db import DbPort 

class MockDb(DbPort):
    
    def get_account_detail_by_username(self, username: str) -> AccountModel:
        pass 
    
    def get_position_by_position_id(self, id_: int) -> PositionModel:
        pass 
    
    def get_status_by_status_id(self, id_: int) -> StatusModel:
        pass 
    
    def create_new_employee(self, new_employee: EmployeeModel) -> int:
        pass 
    
    def get_all_employee(self) -> List[EmployeeModel]:
        pass 
    
    def get_employee_by_id(self, id_: int) -> EmployeeModel:
        pass 
    
    def update_employee(self, update_employee: EmployeeModel) -> int:
        pass 
    
    def create_new_position(self, new_position: PositionModel) -> int:
        pass 
    
    def get_all_position(self) -> List[PositionModel]:
        pass 
    
    def update_position(self, update_position: PositionModel) -> int:
        pass 
    
    def delete_position_by_id(self, id_: int) -> None:
        pass 
    
    def get_department_by_id(self, id_: int) -> DepartmentModel:
        pass 
    
    def create_new_department(self, new_department: DepartmentModel) -> int:
        pass 
    
    def get_all_department(self) -> List[DepartmentModel]:
        pass 
    
    def update_department(self, update_department_model: DepartmentModel) -> int:
        pass 
    
    def delete_department_by_id(self, id_: int) -> None:
        pass 
    
    def create_new_status(self, new_status: StatusModel) -> int:
        pass 
    
    def get_all_status(self) -> List[StatusModel]:
        pass 
    
    def update_status(self, update_status: StatusModel) -> int:
        pass 
    
    def delete_status_by_id(self, id_: int) -> None:
        pass 
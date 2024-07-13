from typing import List
from hexagonalmodel.domain.model.account import AccountModel
from hexagonalmodel.domain.model.employee import EmployeeModel
from hexagonalmodel.domain.model.position import PositionModel
from hexagonalmodel.port.db import DbPort 

class MockDb(DbPort):
    
    def get_account_detail_by_username(self, username: str) -> AccountModel:
        pass 
    
    def get_position_by_position_name(self, position_name: str) -> None:
        pass 
    
    def get_status_by_status_name(self, status: str) -> None:
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
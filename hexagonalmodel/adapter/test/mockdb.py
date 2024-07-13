from hexagonalmodel.domain.model.account import AccountModel
from hexagonalmodel.domain.model.employee import EmployeeModel
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
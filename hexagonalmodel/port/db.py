from abc import ABC,abstractmethod
from hexagonalmodel.domain.model.account import AccountModel
from hexagonalmodel.domain.model.status import StatusModel
from hexagonalmodel.domain.model.position import PositionModel
from hexagonalmodel.domain.model.employee import EmployeeModel
from typing import List

class DbPort(ABC):
    
    @abstractmethod
    def get_account_detail_by_username(self,username: str) -> AccountModel:
        """ get account detail data that match with username

        Args:
            username (str): user name

        Returns:
            AccountModel: model for describe this account
        """   
        
    @abstractmethod
    def get_position_by_position_name(self,position_name: str) -> PositionModel:
        """ get position model in database if not exist should raise InvalidPosition

        Args:
            position_name (str): position name

        Returns:
            PositionModel: position data in database
        """               
        
    @abstractmethod
    def get_status_by_status_name(self,status: str) -> StatusModel:
        """ get status model in database if not exist should raise InvalidStatus

        Args:
            status (str): status

        Returns:
            StatusModel: status data in database
        """        
        
    @abstractmethod
    def create_new_employee(self,new_employee: EmployeeModel) -> int:
        """ create new employee data to database 

        Args:
            new_employee (EmployeeModel): employee model data

        Returns:
            int: id of this employee
        """        
        
    @abstractmethod
    def get_all_employee(self) -> List[EmployeeModel]:
        """ get all employee data in database

        Returns:
            List[EmployeeModel]: list of employee model
        """        
        
    @abstractmethod
    def get_employee_by_id(self,id_: int) -> EmployeeModel:
        """ get employee data from database

        Args:
            id_ (int): id of employee

        Returns:
            EmployeeModel: employee model
        """        
        
    @abstractmethod
    def update_employee(self,update_employee:EmployeeModel) -> int:
        """ update employee data from update employee model to database

        Args:
            update_employee (EmployeeModel): update employee model 

        Returns:
            int: id of employee
        """        
        
    @abstractmethod
    def create_new_position(self,new_position:PositionModel) -> int:
        """ create new position data to database

        Args:
            new_position (PositionModel): new position model

        Returns:
            int: id of this position
        """        
        
    @abstractmethod
    def get_all_position(self) -> List[PositionModel]:
        """ get all position from database

        Returns:
            List[PositionModel]: list of position model
        """        
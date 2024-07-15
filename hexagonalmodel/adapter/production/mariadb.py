from typing import List
from hexagonalmodel.domain.base import exception, settings
from hexagonalmodel.domain.model.account import AccountModel
from hexagonalmodel.domain.model.department import DepartmentModel
from hexagonalmodel.domain.model.employee import EmployeeModel
from hexagonalmodel.domain.model.position import PositionModel
from hexagonalmodel.domain.model.status import StatusModel
from hexagonalmodel.port.db import DbPort
from infrastructure.mariadb.connect import Base,get_db_sess
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class AccountsTable(Base):
    __tablename__ = 'accounts'
    
    id = Column(Integer,primary_key=True)
    username = Column(String(20),nullable=False,unique=True)
    password = Column(String(250),nullable=False)
    employee_owner_id = Column(Integer,ForeignKey(column='employees.id'),nullable=False,unique=True,)
    deactivate = Column(Boolean,default=False)
    
class DepartmentsTable(Base):
    __tablename__ = 'departments'
    
    id = Column(Integer,primary_key=True)
    department_name = Column(String(30),nullable=False,unique=True)
    manager_id = Column(Integer,unique=True)
    
class PositionsTable(Base):
    __tablename__ = 'positions'
    
    id = Column(Integer,primary_key=True)
    position_name = Column(String(30),nullable=False)
    salary = Column(Float,nullable=False)
    department_id = Column(Integer,nullable=False)
    
class StatusTable(Base):
    __tablename__ = 'status'
    
    id = Column(Integer,primary_key=True)
    status_name = Column(String(30),nullable=False,unique=True)
    
class EmployeesTable(Base):
    __tablename__ = 'employees'
    
    id = Column(Integer,primary_key=True)
    first_name = Column(String(40),nullable=False) 
    last_name = Column(String(40),nullable=False) 
    address = Column(String(250),nullable=False) 
    image = Column(String(250))
    
    position_id = Column(Integer,ForeignKey(column='positions.id')) 
    status_id = Column(Integer,ForeignKey(column='status.id')) 
    department_id = Column(Integer,ForeignKey(column='departments.id'))
    
    position = relationship("PositionsTable")
    status = relationship("StatusTable")
    department = relationship("DepartmentsTable")
    
class MariaDbAdapter(DbPort):
    
    def get_account_detail_by_username(self, username: str) -> AccountModel:

        session = get_db_sess()
        row = session.query(AccountsTable).filter_by(username=username).filter(AccountsTable.deactivate != True).first()
        
        if row:
            accountmodel = AccountModel.model_validate(row)
            session.close()
            return accountmodel
        
        session.close()
        raise exception.InvalidAuthorize
    
    def get_position_by_position_id(self, id_: int) -> PositionModel:
        
        session = get_db_sess()
        row = session.query(PositionsTable).filter_by(id=id_).first()
        
        if row:
            positionmodel = PositionModel.model_validate(row)
            session.close()
            return positionmodel
        
        session.close()
        raise exception.InvalidPositionId
    
    def get_status_by_status_id(self, id_: int) -> StatusModel:

        session = get_db_sess()
        row = session.query(StatusTable).filter_by(id=id_).first()
        
        if row:
            statusmodel = StatusModel.model_validate(row)
            session.close()
            return statusmodel
        
        session.close()
        raise exception.InvalidStatusId
    
    def create_new_employee(self, new_employee: EmployeeModel) -> int:

        session = get_db_sess()

        new_row = EmployeesTable(
            first_name = new_employee.first_name,
            last_name = new_employee.last_name,
            address = new_employee.address,
            image = new_employee.image,
            position_id = new_employee.position_id,
            status_id = new_employee.status_id,
            department_id = new_employee.department_id
        )
        
        session.add(new_row)
        session.commit()
        id_ = new_row.id 
        session.close()
        
        return id_ 
    
    def get_all_employee(self) -> List[EmployeeModel]:
        
        session = get_db_sess()
        all_row = session.query(EmployeesTable).all()
        
        list_of_employee = [EmployeeModel.model_validate(row) for row in all_row]
        session.close()
        
        return list_of_employee
    
    def get_employee_by_id(self, id_: int) -> EmployeeModel:
        
        session = get_db_sess()
        row = session.query(EmployeesTable).filter_by(id=id_).first()
        
        if row:
            employeemodel = EmployeeModel.model_validate(row)
            session.close()
            return employeemodel
        
        session.close()
        raise exception.InvalidEmployeeId
    
    def update_employee(self, update_employee: EmployeeModel) -> int:

        session = get_db_sess()
        row = session.query(EmployeesTable).filter_by(id=update_employee.id).first()
        if row:
            is_update = False 
            for key,value in update_employee.model_dump().items():
                if key in ['position','status','department']:
                    continue
                
                elif value and getattr(row,key) != value:
                    setattr(row,key,value)
                    is_update = True
                
                elif value in [0,1,True,False] and getattr(row,key) != value:
                    setattr(row,key,value)
                    is_update = True
                    
                else:
                    continue
            
            if is_update:
                session.commit()
                
            id_ = row.id 
            session.close()
            return id_ 
        
        else:
            session.close()
            raise exception.InvalidEmployeeId 
        
    def create_new_position(self, new_position: PositionModel) -> int:
        
        session = get_db_sess()
        new_row = PositionsTable(**new_position.model_dump())        
        
        session.add(new_row)
        session.commit()
        id_ = new_row.id 
        session.close()
        
        return id_ 
    
    def get_all_position(self) -> List[PositionModel]:

        session = get_db_sess()
        all_row = session.query(PositionsTable).all()
        
        list_of_position = [PositionModel.model_validate(row) for row in all_row]
        session.close()
        
        return list_of_position
    
    def update_position(self, update_position: PositionModel) -> int:

        session = get_db_sess()
        row = session.query(PositionsTable).filter_by(id=update_position.id).first()
        if row:
            is_update = False 
            for key,value in update_position.model_dump().items():
                if value and getattr(row,key) != value:
                    setattr(row,key,value)
                    is_update = True
                
                elif value in [0,1,True,False] and getattr(row,key) != value:
                    setattr(row,key,value)
                    is_update = True
                    
                else:
                    continue
            
            if is_update:
                session.commit()
                
            id_ = row.id 
            session.close()
            return id_ 
        
        else:
            session.close()
            raise exception.InvalidPositionId 
        
    def delete_position_by_id(self, id_: int) -> None:
        
        session = get_db_sess()
        row = session.query(PositionsTable).filter_by(id=id_).first()
        if row:
            employee_already_use_this_position = session.query(EmployeesTable).filter_by(position_id=id_).filter(EmployeesTable.status_id == settings.TERMINATE_STATUS).first()
            if employee_already_use_this_position:
                raise exception.ThisPositionAlreadyUse
            session.delete(row)
            session.commit()
            session.close()
            
        else:
            session.close()
            raise exception.InvalidPositionId 
    
    def get_department_by_id(self, id_: int) -> DepartmentModel:
        
        session = get_db_sess()
        row = session.query(DepartmentsTable).filter_by(id=id_).first()
        
        if row:
            departmentmodel = DepartmentModel.model_validate(row)
            session.close()
            return departmentmodel
        
        session.close()
        raise exception.InvalidDepartmentId       
    
    def create_new_department(self, new_department: DepartmentModel) -> int:
        
        session = get_db_sess()
        new_row = DepartmentsTable(**new_department.model_dump())        
        
        session.add(new_row)
        session.commit()
        id_ = new_row.id 
        session.close()
        
        return id_ 
    
    def get_all_department(self) -> List[DepartmentModel]:

        session = get_db_sess()
        all_row = session.query(DepartmentsTable).all()
        
        list_of_department = [DepartmentModel.model_validate(row) for row in all_row]
        session.close()
        
        return list_of_department
    
    def update_department(self, update_department_model: DepartmentModel) -> int:

        session = get_db_sess()
        row = session.query(DepartmentsTable).filter_by(id=update_department_model.id).first()
        if row:
            is_update = False 
            for key,value in update_department_model.model_dump().items():
                if value and getattr(row,key) != value:
                    setattr(row,key,value)
                    is_update = True
                
                elif value in [0,1,True,False] and getattr(row,key) != value:
                    setattr(row,key,value)
                    is_update = True
                    
                else:
                    continue
            
            if is_update:
                session.commit()
                
            id_ = row.id 
            session.close()
            return id_ 
        
        else:
            session.close()
            raise exception.InvalidDepartmentId
        
    def delete_department_by_id(self, id_: int) -> None:
        session = get_db_sess()
        row = session.query(DepartmentsTable).filter_by(id=id_).first()
        if row:
            
            position_already_use_this_department = session.query(PositionsTable).filter_by(department_id=id_).first()
            if position_already_use_this_department:
                raise exception.ThisDepartmentAlreadyUse
            
            employee_already_use_this_department = session.query(EmployeesTable).filter_by(department_id=id_).filter(EmployeesTable.status_id != settings.TERMINATE_STATUS).first()
            if employee_already_use_this_department:
                raise exception.ThisDepartmentAlreadyUse
            
            session.delete(row)
            session.commit()
            session.close()
            
        else:
            session.close()
            raise exception.InvalidDepartmentId
        
    def create_new_status(self, new_status: StatusModel) -> int:

        session = get_db_sess()
        new_row = StatusTable(**new_status.model_dump())        
        
        session.add(new_row)
        session.commit()
        id_ = new_row.id 
        session.close()
        return id_
        
    def get_all_status(self) -> List[StatusModel]:

        session = get_db_sess()
        all_row = session.query(StatusTable).all()
        
        list_of_status = [StatusModel.model_validate(row) for row in all_row]
        session.close()
        
        return list_of_status
    
    def update_status(self, update_status_model: StatusModel) -> int:

        session = get_db_sess()
        row = session.query(StatusTable).filter_by(id=update_status_model.id).first()
        if row:
            is_update = False 
            for key,value in update_status_model.model_dump().items():
                if value and getattr(row,key) != value:
                    setattr(row,key,value)
                    is_update = True
                
                elif value in [0,1,True,False] and getattr(row,key) != value:
                    setattr(row,key,value)
                    is_update = True
                    
                else:
                    continue
            
            if is_update:
                session.commit()
                
            id_ = row.id 
            session.close()
            return id_ 
        
        else:
            session.close()
            raise exception.InvalidStatusId
        
    def delete_status_by_id(self, id_: int) -> None:

        session = get_db_sess()
        row = session.query(StatusTable).filter_by(id=id_).first()
        if row and row.status_name != 'terminate':
            
            employee_already_use_this_department = session.query(EmployeesTable).filter_by(status_id=id_).first()
            if employee_already_use_this_department:
                raise exception.ThisStatusAlreadyUse
            
            session.delete(row)
            session.commit()
            session.close()
            
        else:
            session.close()
            raise exception.InvalidStatusId
        
    def get_employee_by_filter(self, status_id: int, position_id: int, department_id: int) -> List[EmployeeModel]:

        session = get_db_sess()
        query = session.query(EmployeesTable)
        
        if status_id:
            query.filter(EmployeesTable.status_id == status_id)
            
        if position_id:
            query.filter(EmployeesTable.position_id == position_id)
            
        if department_id:
            query.filter(EmployeesTable.department_id == department_id)
            
        all_row = query.all()
        
        all_employee = [EmployeeModel.model_validate(employee) for employee in all_row]
        
        session.close()
        
        return all_employee
from pytest_mock import MockerFixture
from pytest import raises
from hexagonalmodel.domain.base import exception
from hexagonalmodel.domain import usecase
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.domain import model
from hexagonalmodel.adapter.test.mockdb import MockDb 


mock_employee = model.employee.EmployeeModel(
    first_name='test',
    last_name='test',
    address='test',
    position_id=1,
    status_id=1,
    department_id=1,
    image='test'
)

def test_should_raise_DbAdapterHaveSomethingWrong_when_can_not_get_all_employee_data_in_database(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_call_func = mocker.patch.object(Registry().db,'get_all_employee',side_effect=exception.DbAdapterHaveSomethingWrong)
    
    
    with raises(exception.DbAdapterHaveSomethingWrong):
        all_employee = usecase.employee.get_all_employee()
        
    mock_call_func.assert_called_once()
    
    mocker.resetall()
    
def test_should_not_raise_any_Exception_when_everything_is_valid(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_call_func = mocker.patch.object(Registry().db,'get_all_employee',return_value = list(mock_employee))
    
    all_employee = usecase.employee.get_all_employee()
        
    mock_call_func.assert_called_once()
    
    assert isinstance(all_employee,list)
    
    mocker.resetall()
    
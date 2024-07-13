from pytest_mock import MockerFixture
from pytest import raises
from hexagonalmodel.domain.base import exception
from hexagonalmodel.domain import usecase
from handler import inputbody
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.domain import model
from hexagonalmodel.adapter.test.mockdb import MockDb 
from hexagonalmodel.adapter.test.mockstorage import MockStorage

mock_status = model.status.StatusModel(
    status_name='test'
)
mock_position = model.position.PositionModel(
    position_name='test',
    salary=80000
)
mock_employee = model.employee.EmployeeModel(
    first_name='test',
    last_name='test',
    address='test',
    position=mock_position,
    status=mock_status,
    image='test'
)

def test_should_raise_DbAdapterHaveSomethingWrong_when_can_not_get_all_employee_data_in_database(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_call_func = mocker.patch.object(Registry().db,'get_all_employee',side_effect=exception.DbAdapterHaveSomethingWrong)
    
    
    with raises(exception.DbAdapterHaveSomethingWrong):
        all_employee = usecase.employee.get_all_employee()
        
    mock_call_func.assert_called_once()
    
def test_should_not_raise_any_Exception_when_everything_is_valid(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_call_func = mocker.patch.object(Registry().db,'get_all_employee',return_value = list(mock_employee))
    
    all_employee = usecase.employee.get_all_employee()
        
    mock_call_func.assert_called_once()
    
    assert isinstance(all_employee,list)
    
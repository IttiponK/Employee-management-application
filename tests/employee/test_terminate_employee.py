from pytest_mock import MockerFixture
from pytest import raises
from hexagonalmodel.domain.base import exception
from hexagonalmodel.domain import usecase
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.domain import model
from hexagonalmodel.adapter.test.mockdb import MockDb 
from hexagonalmodel.adapter.test.mockstorage import MockStorage
from handler import inputbody


mock_employee = model.employee.EmployeeModel(
    first_name='test',
    last_name='test',
    address='test',
    position_id=1,
    status_id=1,
    department_id=1,
    image='test'
)

def test_should_raise_DbAdapterHaveSomethingWrong_when_can_not_update_employee_data_to_database(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_request_data = {
        'id':1
    }
    
    
    mock_call_func1 = mocker.patch.object(Registry().db,'get_employee_by_id',return_value=mock_employee)
    
    mock_call_func2 = mocker.patch.object(Registry().db,'update_employee',side_effect=exception.DbAdapterHaveSomethingWrong)
    
    mock_input = inputbody.employee.TerminateEmployee.model_validate(mock_request_data) 
    with raises(exception.DbAdapterHaveSomethingWrong):
        id_ = usecase.employee.terminate_employee(mock_input)
        
    mock_call_func1.assert_called_once()
    mock_call_func2.assert_called_once()
    
    # reset to default value
    mocker.resetall()
        
    
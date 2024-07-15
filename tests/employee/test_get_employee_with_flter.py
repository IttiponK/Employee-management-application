from pytest_mock import MockerFixture
from pytest import raises
from hexagonalmodel.domain.base import exception
from hexagonalmodel.domain import usecase
from handler import inputbody
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.domain import model
from hexagonalmodel.adapter.test.mockdb import MockDb 

def test_should_raise_DbAdapterHaveSomethingWrong_when_can_not_get_employee_from_database(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_request_data = {
        "position_id":1,
        "status_id":1,
        "department_id":1
    }
    
    mock_call_func = mocker.patch.object(Registry().db,'get_employee_by_filter',side_effect=exception.DbAdapterHaveSomethingWrong)
    
    mock_input_body = inputbody.employee.GetEmployeeWithFilter.model_validate(mock_request_data)
    
    with raises(exception.DbAdapterHaveSomethingWrong):
        
        list_of_employee = usecase.employee.get_empolyees_with_filter(mock_input_body)
        
    mock_call_func.assert_called_once()
    
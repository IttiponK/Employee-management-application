from pytest_mock import MockerFixture
from pytest import raises
from hexagonalmodel.domain.base import exception
from hexagonalmodel.domain import usecase
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.domain import model
from hexagonalmodel.adapter.test.mockdb import MockDb 
from handler import inputbody

def test_should_raise_DbAdapterHaveSomethingWrong_when_can_not_create_new_department_to_database(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_request_data = {
        "department_name":"test",
        "manager_id":1
    }
    
    mock_call_func1 = mocker.patch.object(Registry().db,'create_new_department',side_effect=exception.DbAdapterHaveSomethingWrong)
    
    mock_input = inputbody.department.CreateNewDepartment.model_validate(mock_request_data)
    with raises(exception.DbAdapterHaveSomethingWrong):
        id_ = usecase.department.create_new_department(mock_input)
        
    mock_call_func1.assert_called_once()
    
    mocker.resetall()
    
def test_should_not_raise_any_Exception_when_everything_is_valid(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_request_data = {
        "department_name":"test",
        "manager_id":1
    }
    
    mock_call_func1 = mocker.patch.object(Registry().db,'create_new_department',return_value=1)
    
    mock_input = inputbody.department.CreateNewDepartment.model_validate(mock_request_data)

    id_ = usecase.department.create_new_department(mock_input)
        
    mock_call_func1.assert_called_once()
    
    assert isinstance(id_,int)
    
    mocker.resetall()
    
    
    
    
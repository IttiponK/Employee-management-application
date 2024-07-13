from pytest_mock import MockerFixture
from pytest import raises
from hexagonalmodel.domain.base import exception
from hexagonalmodel.domain import usecase
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.domain import model
from hexagonalmodel.adapter.test.mockdb import MockDb 
from hexagonalmodel.adapter.test.mockstorage import MockStorage
from handler import inputbody

def test_should_raise_DbAdapterHaveSomethingWrong_when_can_not_delete_department_from_database(mocker: MockerFixture):
    Registry().db = MockDb() 
    
    mock_request_data = {
        'id':1 
    }
    
    mock_call_func = mocker.patch.object(Registry().db,'delete_department_by_id',side_effect=exception.DbAdapterHaveSomethingWrong)
    
    mock_input = inputbody.department.DeleteDepartment.model_validate(mock_request_data)
    
    with raises(exception.DbAdapterHaveSomethingWrong):
        usecase.department.delete_department(mock_input)
        
    mock_call_func.assert_called_once()
    
    mocker.resetall()
    
def test_should_not_raise_any_Exception_when_everything_is_valid(mocker: MockerFixture):
    Registry().db = MockDb() 
    
    mock_request_data = {
        'id':1 
    }
    
    mock_call_func = mocker.patch.object(Registry().db,'delete_department_by_id',return_value=1)
    
    mock_input = inputbody.department.DeleteDepartment.model_validate(mock_request_data)
    
    usecase.department.delete_department(mock_input)
        
    mock_call_func.assert_called_once()
    
    mocker.resetall()
    
    
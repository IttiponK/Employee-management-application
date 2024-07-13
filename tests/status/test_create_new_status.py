from pytest_mock import MockerFixture
from pytest import raises
from hexagonalmodel.domain.base import exception
from hexagonalmodel.domain import usecase
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.adapter.test.mockdb import MockDb 
from handler import inputbody

def test_should_raise_DbAdapterHaveSomethingWrong_when_can_not_create_new_status_to_database(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_request_body = {
        "status_name":"test"
    }
    
    mock_call_func = mocker.patch.object(Registry().db,'create_new_status',side_effect=exception.DbAdapterHaveSomethingWrong)
    
    mock_input = inputbody.status.CreateNewStatus.model_validate(mock_request_body)
    
    with raises(exception.DbAdapterHaveSomethingWrong):
        id_ = usecase.status.create_new_status(mock_input)
        
    mock_call_func.assert_called_once()
    
    mocker.resetall()
    
def test_should_not_raise_any_Exception_when_everything_is_valid(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_request_body = {
        "status_name":"test"
    }
    
    mock_call_func = mocker.patch.object(Registry().db,'create_new_status',return_value=1)
    
    mock_input = inputbody.status.CreateNewStatus.model_validate(mock_request_body)
    
    id_ = usecase.status.create_new_status(mock_input)
        
    mock_call_func.assert_called_once()
    
    mocker.resetall()
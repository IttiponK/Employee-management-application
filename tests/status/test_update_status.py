from pytest_mock import MockerFixture
from pytest import raises
from hexagonalmodel.domain.base import exception
from hexagonalmodel.domain import usecase
from handler import inputbody
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.domain import model
from hexagonalmodel.adapter.test.mockdb import MockDb 

def test_should_raise_DbAdapterHaveSomethingWrong_when_can_not_update_status_to_database(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_request_data = {
        "id":1,
        "status_name":"test"
    }
    
    mock_call_func = mocker.patch.object(Registry().db,'update_status',side_effect=exception.DbAdapterHaveSomethingWrong)
    
    mock_input = inputbody.status.UpdateStatus.model_validate(mock_request_data)
    with raises(exception.DbAdapterHaveSomethingWrong):
        
        id_ = usecase.status.update_status(mock_input)
        
    mock_call_func.assert_called_once()
    
    mocker.resetall()
    
def test_should_not_raise_any_Exception_when_everything_is_valid(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_request_data = {
        "id":1,
        "status_name":"test"
    }
    
    mock_call_func = mocker.patch.object(Registry().db,'update_status',return_value=1)
    
    mock_input = inputbody.status.UpdateStatus.model_validate(mock_request_data)
        
    id_ = usecase.status.update_status(mock_input)
        
    mock_call_func.assert_called_once()
    
    assert isinstance(id_,int)
    
    mocker.resetall()
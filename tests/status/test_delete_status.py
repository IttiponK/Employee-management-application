from pytest_mock import MockerFixture
from pytest import raises
from hexagonalmodel.domain.base import exception
from hexagonalmodel.domain import usecase
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.adapter.test.mockdb import MockDb 
from handler import inputbody

def test_should_raise_DbAdapterHaveSomethingWrong_when_can_not_delete_status_data_in_database(mocker:MockerFixture):
    Registry().db = MockDb()
    
    mock_request_data = {
        "id":1
    }
    
    mock_call_func = mocker.patch.object(Registry().db,'delete_status_by_id',side_effect=exception.DbAdapterHaveSomethingWrong)

    mock_input = inputbody.status.DeleteStatus.model_validate(mock_request_data)
    
    with raises(exception.DbAdapterHaveSomethingWrong):
        usecase.status.delete_status(mock_input)
        
    mock_call_func.assert_called_once()
    
    mocker.resetall()
    
def test_should_not_raise_any_Exception_when_everything_is_valid(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_request_data = {
        "id":1
    }
    
    mock_call_func = mocker.patch.object(Registry().db,'delete_status_by_id',return_value=None)

    mock_input = inputbody.status.DeleteStatus.model_validate(mock_request_data)
    
    usecase.status.delete_status(mock_input)
        
    mock_call_func.assert_called_once()
    
    mocker.resetall()
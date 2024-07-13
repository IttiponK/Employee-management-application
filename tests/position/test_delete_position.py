from pytest_mock import MockerFixture
from pytest import raises
from hexagonalmodel.domain.base import exception
from hexagonalmodel.domain import usecase
from handler import inputbody
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.adapter.test.mockdb import MockDb 

def test_should_raise_DbAdapterHaveSomethingWrong_when_can_not_delete_position_from_database(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_request_data = {
        "id":1
    }
    
    mock_call_func1 = mocker.patch.object(Registry().db,'delete_position_by_id',side_effect=exception.DbAdapterHaveSomethingWrong)
    
    mock_input = inputbody.position.DeletePosition.model_validate(mock_request_data)
    with raises(exception.DbAdapterHaveSomethingWrong):
        usecase.position.delete_position(mock_input)
        
    mock_call_func1.assert_called_once()
    
    mocker.resetall()
    
def test_should_raise_InvalidPositionId_when_position_id_in_input_data_is_invalid(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_request_data = {
        "id":1
    }
    
    mock_call_func1 = mocker.patch.object(Registry().db,'delete_position_by_id',side_effect=exception.InvalidPositionId)
    
    mock_input = inputbody.position.DeletePosition.model_validate(mock_request_data)
    with raises(exception.InvalidPositionId):
        usecase.position.delete_position(mock_input)
        
    mock_call_func1.assert_called_once()
    
    mocker.resetall()

def test_should_not_raise_any_Exception_when_everythins_is_valid(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_request_data = {
        "id":1
    }
    
    mock_call_func1 = mocker.patch.object(Registry().db,'delete_position_by_id',return_value=None)
    
    mock_input = inputbody.position.DeletePosition.model_validate(mock_request_data)

    usecase.position.delete_position(mock_input)
        
    mock_call_func1.assert_called_once()
    
    mocker.resetall()
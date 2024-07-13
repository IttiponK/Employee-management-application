from pytest_mock import MockerFixture
from pytest import raises
from hexagonalmodel.domain.base import exception
from hexagonalmodel.domain import usecase
from handler import inputbody
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.adapter.test.mockdb import MockDb 

def test_should_raise_DuplicatePosition_when_new_position_already_exist(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mocker_request_data = {
        'position_name':'test',
        'salary':80000.0
    }

    mock_call_func1 = mocker.patch.object(Registry().db,'create_new_position',side_effect=exception.DuplicatePosition)
    
    mock_input = inputbody.position.CreatePosition.model_validate(mocker_request_data)
    with raises(exception.DuplicatePosition):
        usecase.position.create_new_position(mock_input)
        
    mock_call_func1.assert_called_once()
    
    mocker.resetall()
    
def test_should_raise_DbAdapterHaveSomethingWrong_when_can_not_create_new_position_to_database(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mocker_request_data = {
        'position_name':'test',
        'salary':80000.0
    }

    mock_call_func1 = mocker.patch.object(Registry().db,'create_new_position',side_effect=exception.DbAdapterHaveSomethingWrong)
    
    mock_input = inputbody.position.CreatePosition.model_validate(mocker_request_data)
    with raises(exception.DbAdapterHaveSomethingWrong):
        usecase.position.create_new_position(mock_input)
        
    mock_call_func1.assert_called_once()
    
    mocker.resetall()
    
def test_should_not_raise_any_Exception_when_everything_is_valid(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mocker_request_data = {
        'position_name':'test',
        'salary':80000.0
    }

    mock_call_func1 = mocker.patch.object(Registry().db,'create_new_position',return_value=1)
    
    mock_input = inputbody.position.CreatePosition.model_validate(mocker_request_data)
    
    id_ = usecase.position.create_new_position(mock_input)
        
    mock_call_func1.assert_called_once()
    
    assert isinstance(id_,int)
    
    mocker.resetall()
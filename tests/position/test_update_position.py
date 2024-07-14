from pytest_mock import MockerFixture
from pytest import raises
from hexagonalmodel.domain.base import exception
from hexagonalmodel.domain import usecase
from handler import inputbody
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.adapter.test.mockdb import MockDb 

def test_should_raise_InvalidPositionId_when_position_id_in_input_body_is_invalid(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_request_data = {
        'id':999999,
        'position_name':'position_name',
        'salary':80000.0,
        'department_id':None
    }
    
    mock_call_func1 = mocker.patch.object(Registry().db,'update_position',side_effect=exception.InvalidPositionId)
    
    mock_input = inputbody.position.UpdataPosition.model_validate(mock_request_data)
    with raises(exception.InvalidPositionId):
        id_ = usecase.position.update_position(mock_input)
        
    mock_call_func1.assert_called_once()
    
    mocker.resetall()
    
def test_should_not_raise_any_Exception_when_everything_is_valid(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_request_data = {
        'id':1,
        'position_name':'position_name',
        'salary':80000.0,
        'department_id':None
    }
    
    mock_call_func1 = mocker.patch.object(Registry().db,'update_position',return_value=1)
    
    mock_input = inputbody.position.UpdataPosition.model_validate(mock_request_data)
    
    id_ = usecase.position.update_position(mock_input)
    
    mock_call_func1.assert_called_once()
    
    assert isinstance(id_,int) 
    
    mocker.resetall()
    
from pytest_mock import MockerFixture
from pytest import raises
from hexagonalmodel.domain.base import exception
from hexagonalmodel.domain import usecase
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.adapter.test.mockdb import MockDb 
from hexagonalmodel.domain import model

mock_position_model = model.position.PositionModel(
    position_name='test',
    salary=80000
)

def test_should_raise_DbAdapterHaveSomethingWrong_when_can_not_get_all_position_from_database(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_call_func1 = mocker.patch.object(Registry().db,'get_all_position',side_effect=exception.DbAdapterHaveSomethingWrong)
    
    with raises(exception.DbAdapterHaveSomethingWrong):
        all_position = usecase.position.get_all_position()
        
    mock_call_func1.assert_called_once()
    
    mocker.resetall()
    
def test_should_not_raise_any_Exception_when_everything_is_valid(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_call_func1 = mocker.patch.object(Registry().db,'get_all_position',return_value=list(mock_position_model))
    
    all_position = usecase.position.get_all_position()
        
    mock_call_func1.assert_called_once()
    
    assert isinstance(all_position,list)
    
    mocker.resetall()
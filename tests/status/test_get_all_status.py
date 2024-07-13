from pytest_mock import MockerFixture
from pytest import raises
from hexagonalmodel.domain.base import exception
from hexagonalmodel.domain import usecase
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.adapter.test.mockdb import MockDb 
from hexagonalmodel.domain import model

mock_status_model = model.status.StatusModel(
    status_name='test'
)

def test_should_raise_DbAdapterHaveSomethingWrong_when_can_not_get_status_from_database(mocker:MockerFixture):
    Registry().db = MockDb()
    
    mock_call_func = mocker.patch.object(Registry().db,'get_all_status',side_effect=exception.DbAdapterHaveSomethingWrong)

    with raises(exception.DbAdapterHaveSomethingWrong):
        all_status = usecase.status.get_all_status()
        
    mock_call_func.assert_called_once()
    
    mocker.resetall()
    
def test_should_not_raise_any_Exception_when_everything_is_valid(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_call_func = mocker.patch.object(Registry().db,'get_all_status',return_value=list(mock_status_model))

    all_status = usecase.status.get_all_status()
        
    mock_call_func.assert_called_once()
    
    assert isinstance(all_status,list)
    
    mocker.resetall()

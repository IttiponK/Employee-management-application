from pytest_mock import MockerFixture
from pytest import raises
from hexagonalmodel.domain.base import exception
from hexagonalmodel.domain import usecase
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.domain import model
from hexagonalmodel.adapter.test.mockdb import MockDb 

mock_department = model.department.DepartmentModel(
    department_name='information technology'
)

def test_should_raise_DbAdapterHaveSomethingWrong_when_can_not_get_department_data_in_database(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_call_func = mocker.patch.object(Registry().db,'get_all_department',side_effect=exception.DbAdapterHaveSomethingWrong)
    
    with raises(exception.DbAdapterHaveSomethingWrong):
        all_department = usecase.department.get_all_department()
        
    mock_call_func.assert_called_once()
    
    mocker.resetall()
    
def test_should_not_raise_any_Exception_when_everything_is_valid(mocker: MockerFixture):
    
    mock_call_func = mocker.patch.object(Registry().db,'get_all_department',return_value=list(mock_department))
    
    all_department = usecase.department.get_all_department()
        
    mock_call_func.assert_called_once()
    
    assert isinstance(all_department,list)
    
    mocker.resetall()
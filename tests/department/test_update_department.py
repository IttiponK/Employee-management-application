from pytest_mock import MockerFixture
from pytest import raises
from hexagonalmodel.domain.base import exception
from hexagonalmodel.domain import usecase
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.domain import model
from hexagonalmodel.adapter.test.mockdb import MockDb 
from hexagonalmodel.adapter.test.mockstorage import MockStorage
from handler import inputbody

def test_should_raise_InvalidDepartmentId_when_department_id_in_input_body_is_invalid(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_request_data = {
        'id':1,
        'department_name':"test",
        'manager_id':1
    }
    
    mocker_call_func = mocker.patch.object(Registry().db,'update_department',side_effect=exception.DbAdapterHaveSomethingWrong)

    mock_input = inputbody.department.UpdateDepartment.model_validate(mock_request_data)
    with raises(exception.DbAdapterHaveSomethingWrong):
        id_ = usecase.department.update_department(mock_input)
        
    mocker_call_func.assert_called_once()
        
def test_should_not_raise_any_Exception_when_everything_is_valid(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_request_data = {
        'id':1,
        'department_name':"test",
        'manager_id':1
    }
    
    mocker_call_func = mocker.patch.object(Registry().db,'update_department',return_value=1)

    mock_input = inputbody.department.UpdateDepartment.model_validate(mock_request_data)

    id_ = usecase.department.update_department(mock_input)
        
    mocker_call_func.assert_called_once()
    
    assert isinstance(id_,int)
from pytest_mock import MockerFixture
from pytest import raises
from hexagonalmodel.domain.base import exception
from hexagonalmodel.domain import usecase
from handler import inputbody
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.domain import model
from hexagonalmodel.adapter.test.mockdb import MockDb 
from hexagonalmodel.adapter.test.mockstorage import MockStorage

mock_position_model = model.position.PositionModel(
    position_name='test',
    salary=80000
)

mock_status_model = model.status.StatusModel(
    status_name='test'
)

def test_should_raise_InvalidPositoin_when_position_name_in_input_body_is_invalid(mocker:MockerFixture):
    Registry().db = MockDb()
    
    mock_request_data = {
        "first_name":"test",
        "last_name":"test",
        "address":"test address",
        "position_name":"invalid",
        "status":"test",
        "image":b"someimage"
    }
    
    mock_call_func = mocker.patch.object(Registry().db,'get_position_by_position_name',side_effect=exception.InvalidPositoin)
    
    mock_input_body = inputbody.employee.CreateNewEmployee.model_validate(mock_request_data)
    with raises(exception.InvalidPositoin):
        
        id_ = usecase.employee.create_new_employee(mock_input_body)
        
    mock_call_func.assert_called_once()
    
    mocker.resetall()
        
def test_should_raise_DbAdapterHaveSomethingWrong_when_cat_not_check_position_exist_in_db(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_request_data = {
        "first_name":"test",
        "last_name":"test",
        "address":"test address",
        "position_name":"test",
        "status":"test",
        "image":b"someimage"
    }
    
    mock_call_func = mocker.patch.object(Registry().db,'get_position_by_position_name',side_effect=exception.DbAdapterHaveSomethingWrong)
    
    mock_input_body = inputbody.employee.CreateNewEmployee.model_validate(mock_request_data)
    with raises(exception.DbAdapterHaveSomethingWrong):
        
        id_ = usecase.employee.create_new_employee(mock_input_body)
        
    mock_call_func.assert_called_once()
    
    mocker.resetall()
    
def test_should_raise_InvalidStatus_when_status_in_input_body_is_invalid(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_request_data = {
        "first_name":"test",
        "last_name":"test",
        "address":"test address",
        "position_name":"test",
        "status":"invalid",
        "image":b"someimage"
    }
    mock_call_func1 = mocker.patch.object(Registry().db,'get_position_by_position_name',return_value=mock_position_model)
    mock_call_func2 = mocker.patch.object(Registry().db,'get_status_by_status_name',side_effect=exception.InvalidStatus)
    
    mock_input_body = inputbody.employee.CreateNewEmployee.model_validate(mock_request_data)
    with raises(exception.InvalidStatus):
        
        id_ = usecase.employee.create_new_employee(mock_input_body)
    
    mock_call_func1.assert_called_once()  
    mock_call_func2.assert_called_once()
    
    mocker.resetall()
        
def test_should_raise_DbAdapterHaveSomethingWrong_when_can_not_check_status_exist_in_db(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_request_data = {
        "first_name":"test",
        "last_name":"test",
        "address":"test address",
        "position_name":"test",
        "status":"test",
        "image":b"someimage"
    }
    mock_call_func1 = mocker.patch.object(Registry().db,'get_position_by_position_name',return_value=mock_position_model)
    mock_call_func2 = mocker.patch.object(Registry().db,'get_status_by_status_name',side_effect=exception.DbAdapterHaveSomethingWrong)
    
    mock_input_body = inputbody.employee.CreateNewEmployee.model_validate(mock_request_data)
    with raises(exception.DbAdapterHaveSomethingWrong):
        
        id_ = usecase.employee.create_new_employee(mock_input_body)
    
    mock_call_func1.assert_called_once()   
    mock_call_func2.assert_called_once()
    
    mocker.resetall()

def test_should_raise_StorageAdapterHaveSomethingWrong_when_cannot_upload_image_to_storage(mocker: MockerFixture):
    Registry().db = MockDb()
    Registry().storage = MockStorage()
    
    mock_request_data = {
        "first_name":"test",
        "last_name":"test",
        "address":"test address",
        "position_name":"test",
        "status":"test",
        "image":b"someimage"
    }
    
    mock_call_func1 = mocker.patch.object(Registry().db,'get_position_by_position_name',return_value=mock_position_model)
    mock_call_func2 = mocker.patch.object(Registry().db,'get_status_by_status_name',return_value=mock_status_model)
    mock_call_func3 = mocker.patch.object(Registry().storage,'upload_employee_image_file',side_effect=exception.StorageAdapterHaveSomethingWrong)
    
    mock_input_body = inputbody.employee.CreateNewEmployee.model_validate(mock_request_data)
    with raises(exception.StorageAdapterHaveSomethingWrong):
        
        id_ = usecase.employee.create_new_employee(mock_input_body)
    
    mock_call_func1.assert_called_once()
    mock_call_func2.assert_called_once()
    mock_call_func3.assert_called_once()
    
    mocker.resetall()

def test_should_raise_DbAdapterHaveSomethingWrong_when_can_not_create_new_employee_to_db(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_request_data = {
        "first_name":"test",
        "last_name":"test",
        "address":"test address",
        "position_name":"test",
        "status":"test",
        "image":b"someimage"
    }
    
    mock_call_func1 = mocker.patch.object(Registry().db,'get_position_by_position_name',return_value=mock_position_model)
    mock_call_func2 = mocker.patch.object(Registry().db,'get_status_by_status_name',return_value=mock_status_model)
    mock_call_func3 = mocker.patch.object(Registry().storage,'upload_employee_image_file',return_value='test')
    mock_call_func4 = mocker.patch.object(Registry().db,'create_new_employee',side_effect=exception.DbAdapterHaveSomethingWrong)
    
    mock_input_body = inputbody.employee.CreateNewEmployee.model_validate(mock_request_data)
    with raises(exception.DbAdapterHaveSomethingWrong):
        
        id_ = usecase.employee.create_new_employee(mock_input_body)
    
    mock_call_func1.assert_called_once()
    mock_call_func2.assert_called_once()
    mock_call_func3.assert_called_once()  
    mock_call_func4.assert_called_once()
    
    mocker.resetall()
    
def test_should_raise_any_Exception_when_everything_is_valid(mocker: MockerFixture):
    Registry().db = MockDb()
    
    mock_request_data = {
        "first_name":"test",
        "last_name":"test",
        "address":"test address",
        "position_name":"test",
        "status":"test",
        "image":b"someimage"
    }
    
    mock_call_func1 = mocker.patch.object(Registry().db,'get_position_by_position_name',return_value=mock_position_model)
    mock_call_func2 = mocker.patch.object(Registry().db,'get_status_by_status_name',return_value=mock_status_model)
    mock_call_func3 = mocker.patch.object(Registry().storage,'upload_employee_image_file',return_value='test')
    mock_call_func4 = mocker.patch.object(Registry().db,'create_new_employee',return_value=1)
    
    mock_input_body = inputbody.employee.CreateNewEmployee.model_validate(mock_request_data)
        
    id_ = usecase.employee.create_new_employee(mock_input_body)
    
    mock_call_func1.assert_called_once()
    mock_call_func2.assert_called_once()
    mock_call_func3.assert_called_once()  
    mock_call_func4.assert_called_once()
    
    assert isinstance(id_,int)
    
    mocker.resetall()
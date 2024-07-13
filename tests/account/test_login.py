from pytest_mock import MockerFixture
from pytest import raises
from hexagonalmodel.domain.base import exception
from hexagonalmodel.domain import usecase
from handler import inputbody
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.domain import model
from hexagonalmodel.adapter.test.mockdb import MockDb 
from hexagonalmodel.adapter.test.mockencrypt import MockEncrypt

mock_status = model.status.StatusModel(
    status_name='test'
)
mock_position = model.position.PositionModel(
    position_name='test',
    salary=80000
)
mock_employee = model.employee.EmployeeModel(
    first_name='test',
    last_name='test',
    address='test',
    position=mock_position,
    status=mock_status,
    image='test'
)
mock_account = model.account.AccountModel(
    username='test',
    password='test',
    owner=mock_employee,
    deactivate=False
)

def test_should_raise_InvalidAuthorize_when_username_or_password_is_invalid(mocker:MockerFixture):
    Registry().db = MockDb()
    Registry().encryption = MockEncrypt()
    
    mock_request_data = {
        "username":"test",
        "password":"invalid"
    }
    
    mocker.patch.object(Registry().db,'get_account_detail_by_username',return_value = mock_account)
    mocker.patch.object(Registry().encryption,'verify_plaintext',side_effect=exception.InvalidAuthorize)
    
    mock_input = inputbody.account.LoginModel.model_validate(mock_request_data)
    
    with raises(exception.InvalidAuthorize):
        
        usecase.account.login(mock_input)
    
    mocker.resetall()

def test_should_raise_DbAdapterHaveSomethingWrong_when_can_not_get_account_from_database(mocker:MockerFixture):
    Registry().db = MockDb()
    Registry().encryption = MockEncrypt()
    
    mock_request_data = {
        "username":"test",
        "password":"invalid"
    }
    
    mocker.patch.object(Registry().db,'get_account_detail_by_username',side_effect=exception.DbAdapterHaveSomethingWrong)
    
    mock_input = inputbody.account.LoginModel.model_validate(mock_request_data)
    
    with raises(exception.DbAdapterHaveSomethingWrong):
        
        usecase.account.login(mock_input)
        
    mocker.resetall()
        
def test_should_raise_EncryptionAdapterHaveSomethingWrong_when_can_not_verify_plaintext(mocker: MockerFixture):
    Registry().db = MockDb()
    Registry().encryption = MockEncrypt()
    
    mock_request_data = {
        "username":"test",
        "password":"invalid"
    }
    
    mocker.patch.object(Registry().db,'get_account_detail_by_username',return_value = mock_account)
    mocker.patch.object(Registry().encryption,'verify_plaintext',side_effect=exception.EncryptionAdapterHaveSomethingWrong)
    
    mock_input = inputbody.account.LoginModel.model_validate(mock_request_data)
    
    with raises(exception.EncryptionAdapterHaveSomethingWrong):
        
        usecase.account.login(mock_input)
        
    mocker.resetall()
        
def test_should_raise_InvalidAuthorize_when_this_account_is_deactivate(mocker: MockerFixture):
    Registry().db = MockDb()
    Registry().encryption = MockEncrypt()
    
    mock_request_data = {
        "username":"test",
        "password":"invalid"
    }
    
    mock_account.deactivate = True
    mocker.patch.object(Registry().db,'get_account_detail_by_username',return_value = mock_account)
    
    mock_input = inputbody.account.LoginModel.model_validate(mock_request_data)
    
    with raises(exception.InvalidAuthorize):
        
        usecase.account.login(mock_input)
        
    # set to default value 
    mock_account.deactivate = False
    mocker.resetall()
        
def test_should_not_raise_any_Exception_when_everything_is_valid(mocker: MockerFixture):
    Registry().db = MockDb()
    Registry().encryption = MockEncrypt()
    
    mock_request_data = {
        "username":"test",
        "password":"invalid"
    }
    
    mock_call_func1 = mocker.patch.object(Registry().db,'get_account_detail_by_username',return_value = mock_account)
    mock_call_func2 = mocker.patch.object(Registry().encryption,'verify_plaintext')
    
    mock_input = inputbody.account.LoginModel.model_validate(mock_request_data)
    result = usecase.account.login(mock_input)
    
    assert isinstance(result,dict)
    
    assert result == mock_account.model_dump()
    
    mock_call_func1.assert_called_once()
    
    mock_call_func2.assert_called_once()
    
    mocker.resetall()
    
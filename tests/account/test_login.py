from pytest_mock import MockerFixture
from pytest import raises
from hexagonalmodel.domain.base import exception
from hexagonalmodel.domain import usecase
from handler import inputbody

def test_should_raise_InvalidAuthorize_when_username_or_password_is_invalid(mocker:MockerFixture):
    mock_request_data = {
        "username":"test",
        "password":"invalid"
    }
    
    with raises(exception.InvalidAuthorize):
        mock_input = inputbody.account.LoginModel.parse_obj(mock_request_data)
        usecase.account.login(mock_input)

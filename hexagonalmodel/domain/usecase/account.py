from handler import inputbody
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.domain import model
from hexagonalmodel.domain.base import exception

def login(input_body:inputbody.account.LoginModel) -> dict:
    repo = Registry()
    
    user_account = repo.db.get_account_detail_by_username(username=input_body.username)

    repo.encryption.verify_plaintext(plaintext=input_body.password,encrypt=user_account)

    if user_account.deactivate:
        raise exception.InvalidAuthorize
    
    return user_account.model_dump()
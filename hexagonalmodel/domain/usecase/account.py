from handler import inputbody
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.domain.model.account import AccountModel
from hexagonalmodel.domain.base import exception

def login(input_body:inputbody.account.LoginModel) -> AccountModel:
    repo = Registry()
    
    user_account = repo.db.get_account_detail_by_username(username=input_body.username)

    repo.encryption.verify_plaintext(plaintext=input_body.password,encrypt=user_account.password)

    if user_account.deactivate:
        raise exception.InvalidAuthorize
    
    user_account.password = None
    
    return user_account

def get_account_by_id(id_:int) -> AccountModel:
    repo = Registry()
    
    account = repo.db.get_account_by_id(id_=id_)
    
    return account
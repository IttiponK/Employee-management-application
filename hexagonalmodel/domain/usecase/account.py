from handler import inputbody
from hexagonalmodel.domain.base.registry import Registry
from hexagonalmodel.domain import model

def login(input_body:inputbody.account.LoginModel) -> dict:
    repo = Registry()
    
    account_detail = repo.db.get_account_detail_by_username(username=input_body.username)

    # repo.encryption.verify_plaintext(plaintext=input_body.password,encrypt=user_account)

    # if user_account.de
    
    # return user_account.dict()
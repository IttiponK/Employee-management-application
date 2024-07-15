from flask_login import LoginManager,UserMixin
from flask import Flask
from hexagonalmodel.domain.model.account import AccountModel
from hexagonalmodel.domain import usecase
from hexagonalmodel.domain.base import exception


class LoginUser(UserMixin,AccountModel):
    pass


def initial_login_manager(app:Flask):
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(account_id:int):
        print(account_id)
        account = usecase.account.get_account_by_id(id_=account_id)
        login_account = LoginUser.model_validate(account)
        
        return login_account
    
    @login_manager.unauthorized_handler
    def unauthorized_handler():
        raise exception.InvalidAuthorize
    
        

    
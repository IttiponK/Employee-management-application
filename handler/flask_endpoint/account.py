from flask import jsonify, request,Blueprint
from flask_login import login_user
from handler import inputbody
from handler.flask_middleware import decorator,authlogin
from hexagonalmodel.domain import usecase

account_blueprint = Blueprint('account',__name__)

@account_blueprint.route('/login',methods=['POST'])
@decorator.endpoint_handler
def login_endpoint():
    
    input_body = inputbody.account.LoginModel.model_validate(request.get_json())
    profile = usecase.account.login(input_body)
    
    account = authlogin.LoginUser.model_dump(profile)
    login_user(account)
    
    return jsonify(
        {
            'profile': profile
        }
    )
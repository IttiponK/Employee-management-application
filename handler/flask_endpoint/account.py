from flask import jsonify, request,Blueprint

from handler import inputbody
from handler.flask_middleware import decorator
from hexagonalmodel.domain import usecase


account_blueprint = Blueprint('account',__name__)

@account_blueprint.route('/login',methods=['POST'])
@decorator.endpoint_handler
def account_login():
    
    input_body = inputbody.account.LoginModel.model_validate(request.get_json())
    profile = usecase.account.login(input_body)
    
    return jsonify(
        {
            'profile':profile
        }
    )
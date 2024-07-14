from flask import request,Blueprint

account_blueprint = Blueprint('account',__name__)

@account_blueprint.route('/login',methods=['POST'])
def account_login():
    print(request.files.get('file'))
    return request.form
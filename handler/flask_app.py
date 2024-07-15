from flask import Flask
from handler import eventhandler, flask_endpoint as endpoint
from handler.flask_middleware import authlogin
from hexagonalmodel.domain.base import settings

def create_flask_app():
    app = Flask(__name__)
    
    app.secret_key = settings.APP_SECRET
    
    eventhandler.dependency_injection()
    
    authlogin.initial_login_manager(app)
        
    app.register_blueprint(endpoint.account.account_blueprint,url_prefix='/account')
    app.register_blueprint(endpoint.employee.employee_blueprint,url_prefix='/employee')
    app.register_blueprint(endpoint.department.department_blueprint,url_prefix='/department')
    app.register_blueprint(endpoint.position.position_blueprint,url_prefix='/position')
    app.register_blueprint(endpoint.status.status_blueprint,url_prefix='/status')
    
    return app
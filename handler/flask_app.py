from flask import Flask
from handler import eventhandler, flask_endpoint as endpoint


def create_flask_app():
    app = Flask(__name__)
    
    eventhandler.dependency_injection()

    app.register_blueprint(endpoint.account.account_blueprint,url_prefix='/account')
    app.register_blueprint(endpoint.employee.employee_blueprint,url_prefix='/employee')
    app.register_blueprint(endpoint.department.department_blueprint,url_prefix='/department')
    app.register_blueprint(endpoint.position.position_blueprint,url_prefix='/position')
    
    return app
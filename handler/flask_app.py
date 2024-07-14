from flask import Flask
from handler import eventhandler, flask_endpoint


def create_flask_app():
    app = Flask(__name__)
    
    eventhandler.dependency_injection()

    app.register_blueprint(flask_endpoint.account.account_blueprint,url_prefix='/account')
    app.register_blueprint(flask_endpoint.employee.employee_blueprint,url_prefix='/employee')
    app.register_blueprint(flask_endpoint.department.department_blueprint,url_prefix='/department')
    
    return app
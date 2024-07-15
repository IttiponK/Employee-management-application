import json
from flask import Blueprint, jsonify,request
from hexagonalmodel.domain import usecase
from handler import inputbody
from handler.flask_middleware import decorator

employee_blueprint = Blueprint('employee',__name__)

@employee_blueprint.route('/create-new-employee',methods=['POST'])
@decorator.endpoint_handler
def create_new_employee_enpoint():
    input_body = inputbody.employee.CreateNewEmployee(
        first_name=request.form.get('first_name'),
        last_name=request.form.get('last_name'),
        address=request.form.get('address'),
        position_id=request.form.get('position_id'),
        status_id=request.form.get('status_id'),
        department_id=request.form.get('department_id'),
        image=request.files.get('image')
    )
    
    id_ = usecase.employee.create_new_employee(input_body)
    
    return jsonify(
        {
            'employee_id':id_
        }
    ),200
    
    
@employee_blueprint.route('/get-all-employee',methods=['GET'])
@decorator.endpoint_handler
def get_all_employee_endpoint():
    
    all_employee = usecase.employee.get_all_employee()
    
    all_serialize_employee = [employee.model_dump() for employee in all_employee]
    
    return jsonify(
        {
            'all_employee':all_serialize_employee
        }
    ),201
    
@employee_blueprint.route('/update-employee',methods=['PUT'])
@decorator.endpoint_handler
def update_employee_endpoint():
    
    input_body = inputbody.employee.UpdateEmployee.model_validate(request.get_json())
    id_ = usecase.employee.update_employee(input_body)

    return jsonify(
        {
            'employee_id':id_
        }
    ),200

@employee_blueprint.route('/terminate_employee',methods=['DELETE'])
@decorator.endpoint_handler
def terminate_employee_endpoint():
    
    input_body = inputbody.employee.TerminateEmployee.model_validate(request.get_json())
    
    usecase.employee.terminate_employee(input_body)
    
    return jsonify(
        {
            'message':'success'
        }
    )
        
@employee_blueprint.route('/get-employee-with-filter',methods=['POST'])
@decorator.endpoint_handler
def get_employee_with_filter_endpoint():
    
    input_body = inputbody.employee.GetEmployeeWithFilter.model_validate(request.get_json())
    
    all_employee = usecase.employee.get_empolyees_with_filter(input_body)
    
    all_serialize_employee = [employee.model_dump() for employee in all_employee]
    
    return jsonify(
        {
            'all_employee':all_serialize_employee
        }
    )
    
    
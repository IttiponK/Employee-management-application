from flask import Blueprint, jsonify,request

from handler import inputbody
from handler.flask_middleware import decorator
from hexagonalmodel.domain import usecase

department_blueprint = Blueprint('department',__name__)

@department_blueprint.route('/create-new-department',methods=['POST'])
@decorator.endpoint_handler
def create_new_department_endpoint():
    input_body = inputbody.department.CreateNewDepartment.model_validate(request.get_json())
    
    id_ = usecase.department.create_new_department(input_body)
    
    return jsonify(
        {
            'department_id':id_
        }
    )
    
@department_blueprint.route('/get-all-department',methods=['GET'])
@decorator.endpoint_handler
def get_all_department_endpoint():
    
    all_department = usecase.department.get_all_department()
    
    all_serialize_department = [department.model_dump() for department in all_department]
    
    return jsonify(
        {
            'all_department':all_serialize_department
        }
    )
    
@department_blueprint.route('/update-department',methods=['PUT'])
@decorator.endpoint_handler
def update_department_endpoint():
    input_body = inputbody.department.UpdateDepartment.model_validate(request.get_json())
    
    id_ = usecase.department.update_department(input_body)
    
    return jsonify(
        {
            'department_id':id_
        }
    )
    
@department_blueprint.route('/delete-department',methods=['DELETE'])
@decorator.endpoint_handler
def delete_department_endpoint():
    input_body = inputbody.department.DeleteDepartment.model_validate(request.get_json())
    
    usecase.department.delete_department(input_body)
    
    return jsonify(
        {
            'message':'success'
        }
    )
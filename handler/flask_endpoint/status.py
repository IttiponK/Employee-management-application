from flask import Blueprint,request,jsonify
from flask_login import login_required
from handler import inputbody
from handler.flask_middleware import decorator
from hexagonalmodel.domain import usecase

status_blueprint = Blueprint('status',__name__)

@status_blueprint.route('/create-new-status',methods=['POST'])
@decorator.endpoint_handler
@login_required
def create_new_status_endpoint():
    input_body = inputbody.status.CreateNewStatus.model_validate(request.get_json())
    
    id_ = usecase.status.create_new_status(input_body)
    
    return jsonify(
        {
            'status_id':id_
        }
    )
    
@status_blueprint.route('/get-all-status',methods=['GET'])
@decorator.endpoint_handler
@login_required
def get_all_status_endpoint():
    
    all_status = usecase.status.get_all_status()
    
    all_serialize_status = [status.model_dump() for status in all_status]
    
    return jsonify(
        {
            'all_status':all_serialize_status
        }
    )
    
@status_blueprint.route('/update-status',methods=['PUT'])
@decorator.endpoint_handler
@login_required
def update_status_endpoint():
    
    input_body = inputbody.status.UpdateStatus.model_validate(request.get_json())
    
    id_ = usecase.status.update_status(input_body)
    
    return jsonify(
        {
            'status_id':id_
        }
    )
    
@status_blueprint.route('/delete-status',methods=['DELETE'])
@decorator.endpoint_handler
@login_required
def delete_status_endpoint():
    
    input_body = inputbody.status.DeleteStatus.model_validate(request.get_json())
    
    usecase.status.delete_status(input_body)
    
    return jsonify(
        {
            'message':'success'
        }
    )
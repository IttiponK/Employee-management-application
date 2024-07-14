from flask import Blueprint,request,jsonify

from handler import inputbody
from handler.flask_middleware import decorator
from hexagonalmodel.domain import usecase

position_blueprint = Blueprint('position',__name__)

@position_blueprint.route('/create-new-position',methods=['POST'])
@decorator.endpoint_handler
def create_new_position_endpoint():
    
    input_body = inputbody.position.CreatePosition.model_validate(request.get_json())
    id_ = usecase.position.create_new_position(input_body)
    
    return jsonify(
        {
            'position_id':id_
        }
    ),201
    
@position_blueprint.route('/get-all-position',methods=['GET'])
@decorator.endpoint_handler
def get_all_position_endpoint():
    
    all_position = usecase.position.get_all_position()
    
    all_serialize_position = [position.model_dump() for position in all_position]
    
    return jsonify(
        {
            'all_position':all_serialize_position
        }
    ),200
    
@position_blueprint.route('/update-position',methods=['PUT'])
@decorator.endpoint_handler
def update_position_endpoint():
    
    input_body = inputbody.position.UpdataPosition.model_validate(request.get_json())
    
    id_ = usecase.position.update_position(input_body)
    
    return jsonify(
        {
            'position_id':id_
        }
    ),200
    
@position_blueprint.route('/delete-position',methods=['DELETE'])
@decorator.endpoint_handler
def delete_position_endpoint():
    
    input_body = inputbody.position.DeletePosition.model_validate(request.get_json())
    
    usecase.position.delete_position(input_body)
    
    return jsonify(
        {
            'message':'success'
        }
    )
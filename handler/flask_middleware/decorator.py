import functools
from flask import jsonify
from hexagonalmodel.domain.base import exception
from pydantic import ValidationError
from hexagonalmodel.domain.base.logging import logger

def endpoint_handler(func):
    @functools.wraps(func)
    def decorator(*args,**kwargs):
        try:
        
            return func()
        
        except (
            exception.InvalidDepartmentId,
            exception.InvalidPositionId,
            exception.InvalidStatusId,
            ValidationError
        ) as e:
            logger.error('invalid data',exc_info=True)
            return jsonify(
                {
                    "message":"invalid data"
                }
            ),422
        
        except exception.DbAdapterHaveSomethingWrong:
            
            logger.error('DbAdapterHaveSomethingWrong',exc_info=True)
            return jsonify(
                {
                    'message':'database gone'
                }
            ),500
        
        except exception.StorageAdapterHaveSomethingWrong:
            
            logger.error('StorageAdapterHaveSomethingWrong',exc_info=True)
            return jsonify(
                {
                    'message':'cannot upload image to storage'
                }
            ),500
        
        except exception.InvalidAuthorize:
            logger.error('InvalidAuthorize',exc_info=True)
            return jsonify(
                {
                    'message':'not authorize'
                }
            ),401
        
        except Exception as e:
            
            logger.error(str(e),exc_info=True)
            return jsonify(
                {
                    "message":"something wrong"
                }
            ),500
            
    return decorator
from flask import jsonify, make_response, current_app, request
import jwt
from functools import wraps
from models.account import Account
from controllers.util.error import Error, json_response

def verify_token(token):
    
    try:
        token_info = jwt.decode(token,
                                algorithms='HS512',
                                verify=True,
                                key=current_app.config['SECRET_KEY'])
        
        account = Account.query.filter_by(uid=token_info['uid']).first()
        
        if not account:
            return json_response('Error', 401, Error.INVALID_TOKEN.value)
        
        return None
    
    except Exception:
        
        return json_response('Error', 401, Error.INVALID_TOKEN.value)


def token_required(f):
    
    @wraps(f)
    def decored(*args, **kwargs):
        
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return make_response(jsonify(json_response('Error', 401, Error.NON_EXIST_TOKEN.value)), 401)
        
        error_response = verify_token(token)
        
        if error_response:
            return make_response(jsonify(error_response), error_response['code'])
        
        return f(*args, **kwargs)
    
    return decored

def auth_token(token):

    error_response = verify_token(token)
    
    if error_response:
        return error_response
    
    return json_response('OK', 200, 'valid')


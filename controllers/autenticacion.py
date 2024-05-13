from flask import jsonify, make_response, current_app, request
import jwt
from functools import wraps
from models.cuenta import Cuenta
from controllers.util.error import Error, json_error

def token_required(f):
    
    @wraps(f)
    def decored(*args, **kwargs):
        
        token = None

        if 'X-Access-Token' in request.headers:
            token = request.headers['X-Access-Token']

        if not token:
            return make_response(json_error(Error.TOKEN_INEXISTENTE.value, 401), 401)
        
        
        try:
            
            token_info = jwt.decode(token,
                                    algorithms = "HS512",
                                    verify = True, 
                                    key = current_app.config['SECRET_KEY']
                                    )

            cuenta = Cuenta.query.filter_by(uid = token_info['uid']).first()
            
            if not cuenta:
                return make_response(json_error(Error.TOKEN_INVALIDO.value, 401), 401)
            
        except Exception :    
            return make_response(json_error(Error.TOKEN_INVALIDO.value, 401), 401)
        
        return f(*args, **kwargs)
    
    return decored


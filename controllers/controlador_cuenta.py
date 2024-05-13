from models.cuenta import Cuenta
from models.persona import Persona

from .util.error import Error, json_error
from datetime import datetime, timedelta
from flask import jsonify, current_app

from app import Base
import jwt

class ControladorCuenta():
    

    def inicio_sesion(valores):
        
        cuenta = Cuenta.query.filter_by(email = valores.get('email')).first()
        
        if not cuenta:
            return json_error(Error.CUENTA_INEXISTENTE.value, 400)
        
        if cuenta.clave != valores.get('clave'):
            return json_error(Error.CUENTA_INEXISTENTE.value, 400)
        
        token = jwt.encode(
            {
            'uid' : cuenta.uid,
            'exp' : datetime.utcnow() + timedelta(minutes = 5)
            },
            key = current_app.config['SECRET_KEY'],
            algorithm = 'HS512',
        )

        persona = cuenta.persona
        
        return {
            'token'   : token,
            'code'    : 200,
            'persona' : f'{persona.nombre} {persona.apellido}'
        }
    
    
    
    def crear_cuenta(valores, persona):
        
        cuenta = Cuenta()
        
        cuenta.email = valores.get('email')
        cuenta.clave = valores.get('clave')
        cuenta.persona_id = persona
        
        Base.session.add(cuenta)
        Base.session.commit()
    
    def verify_email(email):
        return bool(Cuenta.query.filter_by(email = email).first())
        
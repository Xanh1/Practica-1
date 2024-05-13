from models.persona import Persona
from .controlador_cuenta import ControladorCuenta

from app import Base

from .util.error import Error, json_error
from flask import jsonify

class ControladorPersona():
    
    def crear_persona(valores):
        
        dni = Persona.query.filter_by(dni = valores.get('dni')).first()
        
        if dni:
            return json_error(Error.DNI_EXISTENTE.value, 409)

        if ControladorCuenta.verify_email(valores.get('email')):
            return json_error(Error.EMAIL_EXISTENTE.value, 409)

        persona = Persona()
        
        persona.dni = valores.get('dni')
        persona.nombre = valores.get('nombre')
        persona.apellido = valores.get('apellido')
        
        Base.session.add(persona)
        Base.session.commit()
        
        ControladorCuenta.crear_cuenta(valores, persona.id)
        
        return {
            'msg'     : 'Acción exitosa',
            'code'    : 200,
            'persona' : f'${persona.nombre} ${persona.apellido}',
        }
        
        
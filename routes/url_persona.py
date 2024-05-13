from flask import Blueprint, make_response, request, jsonify
from controllers.controlador_persona import ControladorPersona
from controllers.controlador_cuenta import ControladorCuenta

from schemas.schema import schema_crear_persona, schema_login
from flask_expects_json import expects_json
from controllers.autenticacion import token_required

route_persona = Blueprint('route_persona', __name__)

@route_persona.route('/persona/registro', methods = ['POST'])
@expects_json(schema_crear_persona)
def registro_persona():
    
    valores = request.json
    
    respuesta = ControladorPersona.crear_persona(valores = valores)
    
    return make_response(jsonify(respuesta), respuesta['code'])

@route_persona.route('/login', methods = ['POST'])
@expects_json(schema_login)
def login():
    
    valores = request.json
    
    respuesta = ControladorCuenta.inicio_sesion(valores = valores)

    return make_response(jsonify(respuesta), respuesta['code'])
    

@route_persona.route('/show')
@token_required
def show():
    
    return make_response(jsonify({'msg': 'posi'}), 200)

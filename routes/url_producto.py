from flask import Blueprint, jsonify, make_response, request
from controllers.controlador_producto import ControladorProducto

from schemas.schema import schema_crear_producto, schema_agregar_lote
from flask_expects_json import expects_json
from controllers.autenticacion import token_required

control = ControladorProducto()

route_producto = Blueprint('route_producto', __name__)

@route_producto.route('/producto/registrar', methods = ['POST'])
@token_required
@expects_json(schema_crear_producto)
def registrar_producto():
    
    valores = request.json
    
    respuesta = ControladorProducto.crear_producto(valores = valores)
    
    return make_response(jsonify(respuesta), respuesta['code'])


@route_producto.route('/producto/lote/agregar', methods = ['POST'])
@token_required
@expects_json(schema_agregar_lote)
def agregar_lote():
    
    valores = request.json
    
    respuesta = ControladorProducto.agregar_lote(valores = valores)
    
    return make_response(jsonify(respuesta), respuesta['code'])

@route_producto.route('/producto/lotes')
def stock():
    
    lotes = control.lista_stock()
    
    return make_response(jsonify({
        'msg': 'Ok',
        'code': 200,
        'info': [lote.serialize for lote in lotes],
    }), 200)


@route_producto.route('/producto/buenos')
def lista_productos_buenos():
    
    lotes = control.lista_productos_buenos()
    
    return make_response(jsonify({
        'msg'  : 'Ok',
        'code' : 200,
        'info' : [lote.serialize for lote in lotes]
        
    }), 200)
    
@route_producto.route('/producto/por-expirar')
def lista_productos_por_expirar():
    
    lotes = control.lista_productos_por_expirar()
    
    return make_response(jsonify({
        'msg'  : 'Ok',
        'code' : 200,
        'info' : [lote.serialize for lote in lotes]
        
    }), 200)
    
@route_producto.route('/producto/expirados')
def lista_productos_expirados():
    
    lotes = control.lista_productos_expirados()
    
    return make_response(jsonify({
        'msg'  : 'Ok',
        'code' : 200,
        'info' : [lote.serialize for lote in lotes]
        
    }), 200)
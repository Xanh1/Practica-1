from flask import Blueprint, jsonify, make_response, request
from controllers.controller_product import ControllerProduct

from schemas.schema import schema_create_product, schema_create_batch
from flask_expects_json import expects_json
from controllers.util.authentication import token_required

ctl_product = ControllerProduct()

url_product = Blueprint('url_product', __name__)

@url_product.route('/product/create', methods = ['POST'])
@token_required
@expects_json(schema_create_product)
def create_product():
    
    json = request.json
    
    response = ctl_product.create_product(values = json)
    
    return make_response(jsonify(response), response['code'])


@url_product.route('/batch/create', methods = ['POST'])
@token_required
@expects_json(schema_create_batch)
def create_batch():
    
    json = request.json
    
    response = ctl_product.create_batch(values = json)
    
    return make_response(jsonify(response), response['code'])

@url_product.route('/stock', methods = ['GET'])
def stock():
    
    response = ctl_product.get_stock()
    
    return make_response(jsonify(response), response['code'])


@url_product.route('/stock/<status>',methods = ['GET'])
def get_products(status):
    
    response = ctl_product.get_stock_by_status(status = status)
    
    return make_response(jsonify(response), response['code'])

@url_product.route('/status', methods = ['GET'])
def get_status():

    response = ctl_product.get_status()

    return make_response(jsonify(response), response['code'])
from flask import Blueprint, make_response, request, jsonify, send_from_directory, current_app
from controllers.controller_person import ControllerPerson
from controllers.controller_account import ControllerAccount

from schemas.schema import schema_create_person, schema_login
from flask_expects_json import expects_json

url_person = Blueprint('url_person', __name__)

ctl_person = ControllerPerson()
ctl_account = ControllerAccount()

@url_person.route('/sign-up', methods = ['POST'])
@expects_json(schema_create_person)
def sign_up():
    
    json = request.json
    
    response = ctl_person.create(values = json)
    
    return make_response(jsonify(response), response['code'])

@url_person.route('/sign-in', methods = ['POST'])
@expects_json(schema_login)
def sign_in():
    
    json = request.json
    
    response = ctl_account.login(values = json)

    return make_response(jsonify(response), response['code'])
    

@url_person.route('/upload-avatar/<uid>', methods=['POST'])
def upload_avatar_user(uid):

    files = request.files

    response = ctl_account.upload_avatar(files = files, uid = uid)

    return make_response(jsonify(response), response['code'])


@url_person.route('/avatar/<uid>', methods = ['GET'])
def get_avatar_acc(uid):

    img = ctl_account.get_avatar(uid = uid)

    return send_from_directory(current_app.config['FLASK_MEDIA'], img['context']) 


@url_person.route('/account/<uid>', methods = ['GET'])
def get_account(uid):
    
    response = ctl_account.get_account(uid = uid)
    
    return make_response(jsonify(response), response['code'])
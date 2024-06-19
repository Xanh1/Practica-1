from models.account import Account

from .util.error import Error, json_response

from flask import current_app
from werkzeug.utils import secure_filename

from app import Base
import jwt

import uuid
import os
from datetime import datetime, timedelta

class ControllerAccount():

    def create(self, values, person):

        account = Account(
            username = values['username'],
            password = values['password'],
            person = person
        )

        Base.session.add(account)
        Base.session.commit()
    
    
    def login(self, values):

        account = self.get_by_username(values['username'])

        if not account:
            return json_response('Error', 200, Error.NON_EXISTS_ACCOUNT.value)
        
        if account.password != values['password']:
            return json_response('Error', 200, Error.NON_EXISTS_ACCOUNT.value)
        
        token = jwt.encode(
            {
            'uid' : account.uid,
            'exp' : datetime.utcnow() + timedelta(minutes = 120)
            },
            key = current_app.config['SECRET_KEY'],
            algorithm = 'HS512',
        )

        
        return json_response('OK', 200, {'token': token, 'person': account.person.name, 'account': account.uid })

    def upload_avatar(self, files):

        account = Account.query.filter_by(uid = files['user']).first()

        if not account:
            return json_response('ERROR', 200, Error.NON_EXISTS_ACCOUNT.value)
        
        file = files['file']

        avatar = str(uuid.uuid1()) + '_' + secure_filename(file.filename)

        file.save(os.path.join(current_app.config['FLASK_MEDIA'], avatar))

        account.avatar = avatar

        Base.session.commit()

        return json_response('OK', 200, 'Avatar uploaded successfully')


    def username_exist(self, username):
        return self.get_by_username(username = username) is not None
    
    def get_by_username(self, username):
        return Account.query.filter_by(username = username).first()
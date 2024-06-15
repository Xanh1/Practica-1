from models.person import Person
from .controller_account import ControllerAccount
from app import Base

from .util.error import Error, json_response

ctl_account = ControllerAccount()

class ControllerPerson():
    

    def create(self, values):

        # dni validation
        if self.dni_exist(dni = values['dni']):
            return json_response('Error', 200, Error.DNI_EXISTS.value)

        # username validation
        if ctl_account.username_exist(username = values['username']):
            return json_response('Error', 200, Error.USER_EXIST.value)
        
        # create person
        person = Person(    
            dni = values['dni'],
            name = values['name'],
            last_name = values['last-name']
        )
        
        # save person
        Base.session.add(person)
        Base.session.commit()
        
        # create account
        ctl_account.create(values = values, person = person)
        
        return json_response('OK', 201, 'Person & Account created successfully')


    def dni_exist(self, dni):
        return Person.query.filter_by(dni = dni).first() is not None


    def get_person_uid(self, uid):
        return Person.query.filter_by(uid = uid).first()
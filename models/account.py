from app import Base
import uuid

class Account(Base.Model):
    
    # table name
    __tablename__ = 'accounts'
    
    # fields
    id        = Base.Column(Base.Integer, primary_key = True)
    uid       = Base.Column(Base.String(60), default = str(uuid.uuid4()), nullable = False)
    username  = Base.Column(Base.String(255), nullable = False, unique = True)
    password  = Base.Column(Base.String(50), nullable = False)
    avatar    = Base.Column(Base.String(255), nullable = True)
    person_id = Base.Column(Base.Integer, Base.ForeignKey('people.id'), nullable = False, unique = True)
    
    # parents relationships
    
    # child relationships
    person = Base.relationship('Person', back_populates = 'account')
    
    # methods
    @property
    def serialize(self):
        return {
            'uid'       : self.uid,
            'username'  : self.username,
            'password'  : self.password,
            'name'      : self.person.name,
            'last_name' : self.person.last_name,
        }
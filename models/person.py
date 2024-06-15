from app import Base
import uuid

class Person(Base.Model):
    
    # table name
    __tablename__ = 'people'
    
    # fields
    id        = Base.Column(Base.Integer, primary_key = True)
    uid       = Base.Column(Base.String(60), default = str(uuid.uuid4()), nullable = False)
    dni       = Base.Column(Base.String(10), nullable = False, unique = True)
    name      = Base.Column(Base.String(50), nullable = False)
    last_name = Base.Column(Base.String(50), nullable = False)
    
    # parent relationships
    account = Base.relationship('Account', back_populates = 'person')
    
    # child relationships
    
    # methods
    @property
    def serialize(self):
        return {
            'uid'       : self.uid,
            'dni'       : self.dni,
            'name'      : self.name,
            'last_name' : self.last_name,
        }
from app import Base
import uuid

class Cuenta(Base.Model):
    
    # nombre de la tabla
    __tablename__ = 'cuentas'
    
    # campos
    id         = Base.Column(Base.Integer, primary_key = True)
    uid        = Base.Column(Base.String(60), default = str(uuid.uuid4()), nullable = False)
    email      = Base.Column(Base.String(255), nullable = False, unique = True)
    clave      = Base.Column(Base.String(50), nullable = False)
    persona_id = Base.Column(Base.Integer, Base.ForeignKey('personas.id'), nullable = False, unique = True)
    
    # relaciones padres
    
    # relaciones hijas
    persona = Base.relationship('Persona', back_populates = 'cuenta')
    
    
    # metodos
    @property
    def serialize(self):
        return {
            'uid'   : self.uid,
            'email' : self.email,
            'clave' : self.clave,
        }
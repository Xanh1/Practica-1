from app import Base
import uuid

class Persona(Base.Model):
    
    # nombre de la tabla
    __tablename__ = 'personas'
    
    # campos
    id          = Base.Column(Base.Integer, primary_key = True)
    uid         = Base.Column(Base.String(60), default = str(uuid.uuid4()), nullable = False)
    dni         = Base.Column(Base.String(10), nullable = False, unique = True)
    nombre      = Base.Column(Base.String(50), nullable = False)
    apellido    = Base.Column(Base.String(50), nullable = False)
    
    # relaciones padres
    cuenta = Base.relationship('Cuenta', back_populates = 'persona')
    
    # relaciones hijas
    
    # metodos
    @property
    def serialize(self):
        return {
            'uid'      : self.uid,
            'dni'      : self.dni,
            'nombre'   : self.nombre,
            'apellido' : self.apellido,
        }
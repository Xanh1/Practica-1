from app import Base
import uuid

class Producto(Base.Model):
    
    # nombre de la tabla
    __tablename__ = 'productos'
    
    # campos
    id          = Base.Column(Base.Integer, primary_key=True)
    uid         = Base.Column(Base.String(60), default=str(uuid.uuid4()), nullable=False)
    nombre      = Base.Column(Base.String(60), nullable=False, unique=True)
    descripcion = Base.Column(Base.String(100), nullable=False)
    
    # relaciones padres
    lotes = Base.relationship('Lote', back_populates='producto')
    lista = Base.relationship('ListaProducto', back_populates='producto')
    
    # relaciones hijas
    
    # metodos
    @property
    def serialize(self):
        return {
            'uid'        : self.uid,
            'name'       : self.nombre,
            'decription' : self.descripcion,
        }

    
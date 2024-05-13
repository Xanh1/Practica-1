from app import Base
import uuid

class Factura(Base.Model):
    
    # nombre de la tabla
    __tablename__ = 'facturas'
    
    # campos
    id          = Base.Column(Base.Integer, primary_key=True)
    uid         = Base.Column(Base.String(60), default=str(uuid.uuid4()), nullable=False)
    nro_factura = Base.Column(Base.Integer, nullable=False, unique=True, autoincrement=True)
    cliente     = Base.Column(Base.String(100), nullable = False)
    fecha       = Base.Column(Base.Date, nullable=False)
    monto       = Base.Column(Base.Float, nullable=False)
    
    # relaciones padres
    
    # relaciones hijas
    detalles = Base.relationship('ListaProducto', back_populates='factura')
    
    
    # metodos
    @property
    def serialize(self):
        return {
            'uid'   : self.uid,
            'email' : self.email,
            'clave' : self.clave,
        }

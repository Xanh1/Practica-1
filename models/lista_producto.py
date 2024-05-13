from app import Base
import uuid

class ListaProducto(Base.Model):
    
    # nombre de la tabla
    __tablename__ = 'lista_productos'
    
    # campos
    id            = Base.Column(Base.Integer, primary_key = True)
    uid           = Base.Column(Base.String(60), default = str(uuid.uuid4()), nullable = False)
    nro_productos = Base.Column(Base.Integer, nullable = False)
    monto         = Base.Column(Base.Float, nullable = False)
    producto_id   = Base.Column(Base.Integer, Base.ForeignKey('productos.id'), nullable = False)
    factura_id    = Base.Column(Base.Integer, Base.ForeignKey('facturas.id'), nullable = False)
    
    # relaciones padres
    
    # relaciones hijas
    factura  = Base.relationship('Factura', back_populates = 'detalles')
    producto = Base.relationship('Producto', back_populates = 'lista')
    
    
    # metodos
    @property
    def serialize(self):
        return {
            'uid'   : self.uid,
            'email' : self.email,
            'clave' : self.clave,
        }
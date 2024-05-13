from app import Base
from datetime import date, timedelta

from .estado_producto import EstadoProducto
import uuid

class Lote(Base.Model):
    
    # nombre de la tabla
    __tablename__ = 'lotes'
    
    # campos
    id          = Base.Column(Base.Integer, primary_key = True)
    uid         = Base.Column(Base.String(60), default = str(uuid.uuid4()), nullable = False)
    precio      = Base.Column(Base.Float, nullable = False)
    stock       = Base.Column(Base.Integer, default = 0, nullable = False)
    fecha_exp   = Base.Column(Base.Date, nullable = False)
    estado      = Base.Column(Base.Enum(EstadoProducto), nullable = False, default = EstadoProducto.BUENO.value)
    producto_id = Base.Column(Base.Integer, Base.ForeignKey('productos.id'), nullable = False)
    
    # relaciones padres
    
    # relaciones hijas
    producto = Base.relationship('Producto', back_populates = 'lotes')
    
    # metodos
    @property
    def serialize(self):
        return {
            'uid'      : self.uid,
            'producto' : self.producto.nombre,
            'precio'   : self.precio,
            'stock'    : self.stock,
            'exp_date' : self.fecha_exp,
            'estado'   : self.estado.value,
        }

    def copia(self):
        
        copia = Lote(
            id          = self.id,
            uid         = self.uid,
            precio      = self.precio,
            stock       = self.stock,
            fecha_exp   = self.fecha_exp,
            estado      = self.estado,
            producto_id = self.producto_id,
        )
    
        return copia
    
    def actualizar_estado(self):
        
        fecha_actual = date.today()
        
        dias_faltantes = (self.fecha_exp - fecha_actual).days

        if dias_faltantes <= 0:
            self.estado = EstadoProducto.EXPIRADO.value
        elif dias_faltantes <= 5:
            self.estado = EstadoProducto.POR_EXPIRAR.value
        else:
            self.estado = EstadoProducto.BUENO.value
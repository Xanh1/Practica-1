from models.producto import Producto
from models.estado_producto import EstadoProducto
from models.lote import Lote
from datetime import date, timedelta
from flask import current_app

from .util.error import Error, json_error
from app import Base

class ControladorProducto():
    
    # get methods
        
    def lista_stock(self):
        
        self.actualizar_lotes()
        
        stock = []
        
        for lote in Lote.query.all():
            
            if lote.estado != EstadoProducto.EXPIRADO:
                stock.append(lote)
        
        return stock
    
    def lista_productos_buenos(self):
        
        self.actualizar_lotes()
        
        return Lote.query.filter_by(estado = EstadoProducto.BUENO)
    
    
    def lista_productos_por_expirar(self):
        
        self.actualizar_lotes()
        
        return Lote.query.filter_by(estado = EstadoProducto.POR_EXPIRAR)
    
    
    def lista_productos_expirados(self):
        
        self.actualizar_lotes()
        
        return Lote.query.filter_by(estado = EstadoProducto.EXPIRADO)
    
    
    def actualizar_lotes(self):
        
        lotes = Lote.query.all()
        
        for lote in lotes:
            
            lote.actualizar_estado()
            
            Base.session.commit()

    
    # create methods
    
    def crear_producto(valores):
        
        nombre = Producto.query.filter_by(nombre = valores.get('nombre')).first()
        
        if nombre:
            return json_error(Error.PRODUCTO_EXISTENTE.value, 409)
        
        producto = Producto()
        
        producto.nombre = valores.get('nombre')
        producto.descripcion = valores.get('descripcion')
        
        Base.session.add(producto)
        Base.session.commit()
        
        return {
            'msg'      : 'Producto registrado',
            'code'     : 200,
            'producto' : producto.uid,
        }
    
    def agregar_lote(valores):
        
        lote = Lote()
        
        producto = Producto.query.filter_by(uid = valores.get('producto')).first()
        
        if not producto:
            return json_error(Error.PRODUCTO_INEXISTENTE.value, 404)
        
        lote.precio = valores.get('precio')
        lote.stock = valores.get('cantidad')
        lote.fecha_exp = valores.get('fecha_exp')
        lote.producto_id = producto.id
        
        Base.session.add(lote)
        Base.session.commit()
        
        return {
            'msg'  : 'Lote registrado',
            'code' : 200,
            'lote' : lote.uid,
        }

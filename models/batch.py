from app import Base
from datetime import date

from .product_status import ProductStatus
import uuid

class Batch(Base.Model):
    
    # table name
    __tablename__ = 'batches'
    
    # fields
    id         = Base.Column(Base.Integer, primary_key = True)
    uid        = Base.Column(Base.String(60), default = str(uuid.uuid4()), nullable = False)
    price      = Base.Column(Base.Float, nullable = False)
    stock      = Base.Column(Base.Integer, default = 0, nullable = False)
    exp_date   = Base.Column(Base.Date, nullable = False)
    status     = Base.Column(Base.Enum(ProductStatus), nullable = False, default = ProductStatus.FRESH.value)
    product_id = Base.Column(Base.Integer, Base.ForeignKey('products.id'), nullable = False)
    
    # parent relationships 
    
    # child relationships
    product = Base.relationship('Product', back_populates = 'batches')
    
    # methods
    @property
    def serialize(self):
        return {
            'uid'      : self.uid,
            'product' : self.product.name,
            'price'    : self.price,
            'stock'    : self.stock,
            'exp_date' : self.exp_date,
            'status'   : self.status.value,
        }
    
    def actualizar_estado(self):
        
        current_date = date.today()
        
        days_left = (self.exp_date - current_date).days

        if days_left <= 0:
            self.status = ProductStatus.EXPIRED.value
        elif days_left <= 5:
            self.status = ProductStatus.NEAR_EXPIRY.value
        else:
            self.status = ProductStatus.FRESH.value
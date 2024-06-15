from app import Base
import uuid

class ProductList(Base.Model):
    
    # fields
    __tablename__ = 'product_list'
    
    # fields
    id         = Base.Column(Base.Integer, primary_key = True)
    uid        = Base.Column(Base.String(60), default = str(uuid.uuid4()), nullable = False)
    number     = Base.Column(Base.Integer, nullable = False)
    amount     = Base.Column(Base.Float, nullable = False)
    product_id = Base.Column(Base.Integer, Base.ForeignKey('products.id'), nullable = False)
    invoice_id = Base.Column(Base.Integer, Base.ForeignKey('invoices.id'), nullable = False)
    
    # parent relationships
    
    # child relationships
    invoice  = Base.relationship('Invoice', back_populates = 'details')
    product = Base.relationship('Product', back_populates = 'list')
    
    
    # methods
    @property
    def serialize(self):
        return {
            'uid'     : self.uid,
            'number'  : self.number,
            'amount'  : self.amount,
            'invoice' : self.invoice.number,
            'product' : self.product.name,
        }
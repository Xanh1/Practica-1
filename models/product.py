from app import Base
import uuid

class Product(Base.Model):
    
    # table name
    __tablename__ = 'products'
    
    # fields
    id          = Base.Column(Base.Integer, primary_key=True)
    uid         = Base.Column(Base.String(60), default=str(uuid.uuid4()), nullable=False)
    name        = Base.Column(Base.String(60), nullable=False, unique=True)
    description = Base.Column(Base.String(100), nullable=False)
    
    # parent relationships 
    batches = Base.relationship('Batch', back_populates='product')
    list    = Base.relationship('ProductList', back_populates='product')
    
    # child relationships
    
    # metodos
    @property
    def serialize(self):
        return {
            'uid'        : self.uid,
            'name'       : self.name,
            'description' : self.description,
        }

    
from app import Base
import uuid

class Invoice(Base.Model):
    
    # table name
    __tablename__ = 'invoices'
    
    # fields
    id     = Base.Column(Base.Integer, primary_key=True)
    uid    = Base.Column(Base.String(60), default=str(uuid.uuid4()), nullable=False)
    number = Base.Column(Base.Integer, nullable=False, unique=True, autoincrement=True)
    client = Base.Column(Base.String(100), nullable = False)
    date   = Base.Column(Base.Date, nullable=False)
    amount = Base.Column(Base.Float, nullable=False)
    
    # parents relationships
    
    # child relationships
    details = Base.relationship('ProductList', back_populates='invoice')
    
    
    # methods
    @property
    def serialize(self):
        return {
            'uid'     : self.uid,
            'number'  : self.number,
            'client'  : self.client,
            'date'    : self.date,
            'amount'  : self.date,
            'details' : [detail.serialize for detail in self.details],
        }

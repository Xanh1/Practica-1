from models.product import Product
from models.product_status import ProductStatus
from models.batch import Batch
from app import Base

from .util.error import Error, json_response

class ControllerProduct():
    
    def get_stock(self):
        
        self.update_batches()
        
        stock = []
        
        for lote in Batch.query.all():
            
            if lote.estado != ProductStatus.EXPIRED:
                stock.append(lote)
        
        return json_response('OK', 200, [batch.serialize for batch in stock])
    
    
    def get_stock_by_status(self, status):

        self.update_batches()

        products = Batch.query.filter_by(status = status)

        return json_response('OK', 200, [product.serialize for product in products])
    
    def get_status(self):

        status = [status.value for status in ProductStatus]

        return json_response('OK', 200, status)

    
    def update_batches(self):
        
        batches = Batch.query.all()
        
        for batch in batches:
            
            batch.actualizar_estado()
            
            Base.session.commit()

    
    # create methods
    
    def create_product(self, values):
        
        name = Product.query.filter_by(name = values['name']).first()
        
        if name:
            return json_response('ERROR', 200, Error.PRODUCT_EXISTS.value)
        
        product = Product(
            name = values['name'],
            description = values['description']
        )
        
        Base.session.add(product)
        Base.session.commit()
        
        return json_response('OK', 200, 'Product created successfully')
    
    def create_batch(self, values):
        
        
        product = Product.query.filter_by(uid = values['product']).first()
        
        if not product:
            return json_response('ERROR', 200, Error.NON_EXIST_PRODUCT.value)
        
        batch = Batch(
            price = values['price'],
            stock = values['stock'],
            exp_date = values['exp_date'],
            product = product
        )
        
        Base.session.add(batch)
        Base.session.commit()
        
        return json_response('OK', 200, 'Batch created successsfully')

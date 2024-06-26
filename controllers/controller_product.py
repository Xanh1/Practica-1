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
            
            if lote.status != ProductStatus.EXPIRED:
                stock.append(lote)
        
        return json_response('OK', 200, [batch.serialize for batch in stock])
    
    def get_product_by_uid(self, uid):

        product = Product.query.filter_by(uid = uid).first()

        return json_response('OK', 200, product.serialize)

    def get_products(self):

        products = Product.query.all()

        return json_response('OK', 200, [product.serialize for product in products])

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
            
            batch.update_status()
            
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
    
    def update_product(self, values):

        product = Product.query.filter_by(uid = values['uid']).first()

        name = Product.query.filter_by(name = values['name']).first()
        
        if name and product.name != name.name:
            return json_response('ERROR', 200, Error.PRODUCT_EXISTS.value)
        
        product.name = values['name']
        product.description = values['description']

        Base.session.commit()

        return json_response('OK', 200, 'Product updated successfully')
    
    def create_batch(self, values):
        
        product = Product.query.filter_by(name = values['product']).first()
        
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

    
    def update_batch(self, values):
        
        product = Product.query.filter_by(name = values['product']).first()
        
        if not product:
            return json_response('ERROR', 200, Error.NON_EXIST_PRODUCT.value)
        
        batch = Batch.query.filter_by(uid = values['batch']).first()
        
        batch.product = product
        batch.price = values['price']
        batch.stock = values['stock']
        batch.exp_date = values['exp_date']
        
        Base.session.commit()
        
        return json_response('OK', 200, 'Batch updated successfully')
        
    def get_batch_by_uid(self, uid):
        
        batch = Batch.query.filter_by(uid = uid).first()
        
        return json_response('OK', 200, batch.serialize)
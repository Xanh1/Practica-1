from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
from init_base import init

Base = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config = False)

    #TODO
    app.config.from_object('config.config.Config')
    
    Base.init_app(app)
    
    with app.app_context():
        from routes.route_person import url_person
        from routes.route_product import url_product
        
        app.register_blueprint(url_person)
        app.register_blueprint(url_product)
        
        init()
        # create db tables
        Base.create_all()
        #Base.drop_all()
    
    return app
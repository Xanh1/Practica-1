from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
from tablas import init

Base = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config = False)

    #TODO
    app.config.from_object('config.config.Config')
    
    Base.init_app(app)
    
    with app.app_context():
        from routes.url_persona import route_persona
        from routes.url_producto import route_producto
        
        app.register_blueprint(route_persona)
        app.register_blueprint(route_producto)
        
        init()
        # create db tables
        Base.create_all()
    
    return app
from app.config import Config
from app.db import db
from app.routes.product_routes import product_route
from flask import Flask
from flask_migrate import Migrate


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(product_route)

    return app

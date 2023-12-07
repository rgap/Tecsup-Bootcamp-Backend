# app.py

from app.routes.product_routes import product_route
from flask import Flask

# other imports if necessary


def create_app():
    app = Flask(__name__)
    # app configuration
    app.register_blueprint(product_route)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

# app.py
from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from utils import response_error, response_success  # Import utility functions

app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@127.0.0.1:3306/mvc_example"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)


# Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.String(120))

    def __init__(self, price):
        self.price = price

    def update_price(self, new_price):
        self.price = new_price


# View is handled by Flask templates (HTML)


# Controller for Displaying the Product's Price
@app.route("/product", methods=["GET"])
def get_product():
    try:
        product = Product.query.first()
        price = product.price if product else None
        return response_success({"price": price})
    except Exception as e:
        return response_error(str(e), 500)


# Controller for Updating the Product's Price
@app.route("/product", methods=["POST"])
def update_product():
    try:
        new_price = request.json.get("price")
        product = Product.query.first()
        if product:
            product.update_price(new_price)
        else:
            product = Product(price=new_price)
            db.session.add(product)
        db.session.commit()
        return response_success({"message": "Price updated successfully"})
    except Exception as e:
        return response_error(str(e), 500)


if __name__ == "__main__":
    app.run(debug=True)

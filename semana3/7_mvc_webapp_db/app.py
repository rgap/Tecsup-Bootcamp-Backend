from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@127.0.0.1:3306/mvc_example"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)


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
    product = Product.query.first()
    price = product.price if product else None
    return render_template("index.html", price=price)


# Controller for Updating the Product's Price
@app.route("/product", methods=["POST"])
def update_product():
    new_price = request.form.get("price")
    product = Product.query.first()
    if product:
        product.update_price(new_price)
    else:
        product = Product(price=new_price)
        db.session.add(product)
    db.session.commit()
    return redirect(url_for("get_product"))


if __name__ == "__main__":
    app.run(debug=True)

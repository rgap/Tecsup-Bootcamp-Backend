from app.db import db
from app.models.product import Product
from flask import Blueprint, redirect, render_template, request, url_for

product_route = Blueprint("product_route", __name__, template_folder="../templates")


@product_route.route("/product", methods=["GET"])
def get_product():
    product = Product.query.first()
    price = product.price if product else None
    return render_template("index.html", price=price)


@product_route.route("/product", methods=["POST"])
def update_product():
    new_price = request.form.get("price")
    product = Product.query.first()
    if product:
        product.update_price(new_price)
    else:
        product = Product(price=new_price)
        db.session.add(product)
    db.session.commit()
    return redirect(url_for("product_route.get_product"))

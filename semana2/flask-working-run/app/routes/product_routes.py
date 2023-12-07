# app/routes/product_routes.py

from flask import Blueprint

product_route = Blueprint("product_route", __name__)


@product_route.route("/products")
def products():
    return "List of products"

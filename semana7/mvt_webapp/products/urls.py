from django.urls import path

from .views import get_product, update_product

urlpatterns = [
    path(
        "", get_product, name="get_product"
    ),  # Routes to the view displaying the product
    path(
        "update/", update_product, name="update_product"
    ),  # Routes to the view updating the product
]

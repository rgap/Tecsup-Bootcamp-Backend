from django.shortcuts import redirect, render

from .models import Product

# Ensure a Product instance exists
if not Product.objects.exists():
    Product.objects.create()

product = Product.objects.first()


# View: Handles web requests and returns web responses
def get_product(request):
    # Retrieves data and passes it to the template (MVT View)
    return render(request, "products/index.html", {"price": product.get_price()})


def update_product(request):
    # Processes data and redirects or renders a template (MVT View)
    if request.method == "POST":
        new_price = request.POST.get("price")
        product.update_price(new_price)
    return redirect("get_product")

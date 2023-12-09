from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


# Model
class Product:
    def __init__(self):
        self.price = ""

    def update_price(self, new_price):
        self.price = new_price

    def get_price(self):
        return self.price


product = Product()

# View is handled by Flask templates (HTML)


# Controller for Displaying the Product's Price
@app.route("/products", methods=["GET"])
def get_product():
    return render_template("index.html", price=product.get_price())


# Controller for Updating the Product's Price
@app.route("/products", methods=["POST"])
def update_product():
    new_price = request.form.get("price")
    product.update_price(new_price)
    return redirect(url_for("get_product"))


if __name__ == "__main__":
    app.run(debug=True)

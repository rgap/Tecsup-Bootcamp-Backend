from flask import Flask, render_template, request, redirect, url_for

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

# Controller
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', price=product.get_price())
    elif request.method == 'POST':
        new_price = request.form.get('price')
        product.update_price(new_price)
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

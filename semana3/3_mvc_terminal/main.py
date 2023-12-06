class Product:
    def __init__(self):
        self.price = ""

    def update_price(self, new_price):
        self.price = new_price

    def get_price(self):
        return self.price


class View:
    def display_price(self, price):
        print(f"Price: {price}")


class Controller:
    def __init__(self, product, view):
        self.product = product
        self.view = view

    def handle_price_update(self, new_price):
        self.product.update_price(new_price)

    def update_view(self):
        price = self.product.get_price()
        self.view.display_price(price)


# Create instances of the Product and View
product = Product()
view = View()

# Create a Controller instance with the Product and View
controller = Controller(product, view)

# Update the price through the Controller
controller.handle_price_update("9.99")

# Display the price
controller.update_view()

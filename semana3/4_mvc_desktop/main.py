import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton

# Model
class Product:
    def __init__(self):
        self.price = ""

    def update_price(self, new_price):
        self.price = new_price

    def get_price(self):
        return self.price

# View
class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('MVC Example')
        self.setGeometry(100, 100, 200, 100)

        self.label = QLabel('Price:', self)
        self.textbox = QLineEdit(self)
        self.button = QPushButton('Update', self)
        self.button.clicked.connect(self.on_update_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.textbox)
        layout.addWidget(self.button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def set_controller(self, controller):
        self.controller = controller

    def on_update_button_clicked(self):
        self.controller.handle_price_update(self.textbox.text())

    def display_price(self, price):
        self.label.setText(f"Price: {price}")

# Controller
class Controller:
    def __init__(self, product, view):
        self.product = product
        self.view = view
        self.view.set_controller(self)

    def handle_price_update(self, new_price):
        self.product.update_price(new_price)
        self.update_view()

    def update_view(self):
        price = self.product.get_price()
        self.view.display_price(price)

# Main application logic
if __name__ == '__main__':
    app = QApplication(sys.argv)
    product = Product()
    view = View()
    controller = Controller(product, view)

    # GUI for user interaction
    view.show()
    sys.exit(app.exec_())

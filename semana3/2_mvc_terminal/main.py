class Model:
    def __init__(self):
        self.data = ""

    def update_data(self, new_data):
        self.data = new_data

    def get_data(self):
        return self.data

class View:
    def display_data(self, data):
        print(f"Data: {data}")

    def get_user_input(self):
        return input("Enter new data: ")

    def set_controller(self, controller):
        self.controller = controller

    def capture_user_action(self):
        self.controller.update_model_data(self.get_user_input())

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controller(self)

    def update_model_data(self, new_data):
        self.model.update_data(new_data)
        self.display_view()

    def display_view(self):
        data = self.model.get_data()
        self.view.display_data(data)

# Main application logic
if __name__ == '__main__':
    model = Model()
    view = View()
    controller = Controller(model, view)

    # Simulate user interaction
    while True:
        view.capture_user_action()

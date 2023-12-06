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


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_model_data(self, new_data):
        self.model.update_data(new_data)

    def display_view(self):
        data = self.model.get_data()
        self.view.display_data(data)


# Create instances of the Model and View
model = Model()
view = View()

# Create a Controller instance with the Model and View
controller = Controller(model, view)

# Update the data through the Controller
controller.update_model_data("Hello MVC!")

# Display the data
controller.display_view()

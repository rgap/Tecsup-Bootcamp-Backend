# Importing the Flask class from the flask module
from db import db
from flask import Flask

# Creating an instance of the Flask class. '__name__' is a special variable in Python
# that is used as the name of the current module. In this case, it will represent
# the name of the application.
app = Flask(__name__)
db.init_app(app)


# The '@app.route' decorator is used to bind the URL '/' (the root of the site)
# to a Python function. In Flask, routes are used to map different URLs to different
# view functions.
@app.route("/")
def index():
    # This is the view function for the root URL. When a user accesses the root URL
    # ('http://localhost:5000/' by default), this function is called and its return
    # value is sent back to the client as a response.
    # Here, it returns a string that will be displayed on the client's web browser.
    return "Mi API REST con Flask"


# The following conditional is a common Python idiom. It checks if the script is
# being run directly (as opposed to being imported as a module in another script).
# '__name__' is set to '__main__' when the script is executed directly.
if __name__ == "__main__":
    # app.run() starts the Flask web server. It enables the app to listen for incoming requests.
    # The 'debug=True' argument enables Flask's debugger. It will reload the server automatically
    # on code changes and provides a debugger console in the browser in case of unhandled exceptions.
    # The 'port=8000' (commented out) would change the default port from 5000 to 8000 if uncommented.
    app.run(debug=True)

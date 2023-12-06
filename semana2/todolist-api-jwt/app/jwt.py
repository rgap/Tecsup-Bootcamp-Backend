from flask_jwt_extended import JWTManager
from utils import response_error

# Creating an instance of JWTManager. This instance will be configured
# to manage JWT settings and callbacks in the Flask application.
jwt = JWTManager()


# This decorator registers a callback function with JWTManager that
# is called when a request is made without a valid JWT token.
@jwt.unauthorized_loader
def unauthorized_callback(callback):
    # The function to handle unauthorized access.
    # It calls the response_error function, passing the callback argument.
    # Note: Typically, the unauthorized loader callback doesn't take arguments
    # in Flask-JWT-Extended. The 'callback' argument's purpose is unclear
    # without additional context - it might be a design choice or an error.
    return response_error(callback)

from flask import Flask

def create_app():
    app = Flask(__name__)
    from . import routes  # Import the routes
    return app
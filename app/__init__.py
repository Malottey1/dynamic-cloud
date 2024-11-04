from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register the blueprint
    from .routes import main  # Ensure your routes module and main blueprint exist
    app.register_blueprint(main)

    return app
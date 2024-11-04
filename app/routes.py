from flask import Blueprint, render_template

# Define a blueprint for the main application
main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Render the index page."""
    return render_template('index.html')

@main.route('/yamal')
def yamal():
    """Render the Lamine Yamal page."""
    return render_template('yamal.html')

@main.route('/musiala')
def musiala():
    """Render the Jamal Musiala page."""
    return render_template('musiala.html')

@main.route('/bellingham')
def bellingham():
    """Render the Jude Bellingham page."""
    return render_template('bellingham.html')

@main.route('/pedri')
def pedri():
    """Render the Pedri page."""
    return render_template('pedri.html')

@main.errorhandler(404)
def page_not_found(e):
    """Render a custom 404 error page."""
    return render_template('404.html'), 404
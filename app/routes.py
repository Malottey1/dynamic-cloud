from flask import Blueprint, render_template

# Define a blueprint
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/yamal')
def yamal():
    return render_template('yamal.html')

@main.route('/musiala')
def musiala():
    return render_template('musiala.html')

@main.route("/bellingham")
def bellingham():
    return render_template("bellingham.html")

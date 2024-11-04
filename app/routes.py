from flask import render_template
from . import create_app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/yamal')
def yamal():
    return render_template('yamal.html') 

@app.route('/bellingham')
def bellingham():
    return render_template('bellingham.html') 
from flask import Flask  # [this is flask module]

app = Flask(__name__)

@app.route('/')
def index()->None:
    """this is a index file
    """
    return "Hello World"

@app.route('/hello')
def hello()->None:
    """this is a hello function
    """
    return "hey World"
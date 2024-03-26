from core import create_app

app = create_app()


@app.route("/")
def index() -> None:
    """this is a index file"""
    return "Hello World"


@app.route("/hello")
def hello() -> None:
    """this is a hello function"""
    return "hey World"

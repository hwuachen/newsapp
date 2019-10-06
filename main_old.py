from flask import Flask

# main entry application
# __name__ is special name to identify current module to render
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return "<h1>Hello!!</h1>"

from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine


app = Flask(__name__)

# pass the config class to app object
# so run this applications by loading the configuration file.
app.config.from_object(Config)

# set the initialization app to the App
db = MongoEngine()
db.init_app(app)

from application import routes

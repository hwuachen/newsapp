from flask import Flask, render_template, request
from config import Config
from flask_mongoengine import MongoEngine

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_bot = ChatBot("Annabot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english.conversations")

# pass the config class to app object
# so run this applications by loading the configuration file.
app.config.from_object(Config)

# set the initialization app to the App
db = MongoEngine()
db.init_app(app)

from application import routes

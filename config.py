import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"

    # set up a MongoDB database
    MONGODB_SETTINGS = {'db': 'News',
                        'host' : 'mongodb://localhost:27017/News'}

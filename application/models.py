import flask
from application import db

class User(db.Document):
    user_id = db.IntField(unique=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    email = db.StringField(max_length=30)
    password = db.StringField(max_length=30)


class Trumptweet(db.Document):
    source = db.StringField(max_length=50)
    id_str = db.StringField(max_length=50)
    text = db.StringField(max_length=280)
    created_at = db.StringField(max_length=50)
    retweet_count = db.IntField(max_length=50)
    in_reply_to_user_id_str = db.StringField(max_length=50)
    favorite_count = db.IntField(max_length=50)
    is_retweet = db.BooleanField(max_length=50)
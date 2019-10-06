from application import app, db
from flask import render_template, request, json, Response
from trumptweets_testdata import trumpTweetsTestData
from application.models import User, Trumptweet

trumpTweets = Trumptweet.objects.all()

def getDataItem(id, data):
    for dataItem in data:
        if id == dataItem['id_str']:
            return dataItem['id_str']

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True)


@app.route("/tweets/")
@app.route("/tweets/<year>")
def tweets(year="2018"):
    print(trumpTweets[0]["id_str"])
    '''passing data from source to view '''
    return render_template("tweet.html", dataList=trumpTweets, tweet=True, year=year, total=len(trumpTweets))


@app.route("/login")
def login():
    return render_template("login.html", login=True)


@app.route("/register")
def register():
    return render_template("register.html", register=True)


@app.route("/view", methods=["GET", "POST"])
def view():
    '''
    # GET
    id = request.args.get('courseID')
    title = request.args.get('title')
    term = request.args.get('term')
    '''
    # POST
    id_str = request.form.get('id_str')
    data = trumpTweetsTestData[0]
    print('id_str =', id_str)
    print(getDataItem(id_str, trumpTweetsTestData))
    return render_template("view.html", view=True, data=data)


@app.route("/test/")
@app.route("/test/<idx>")
def test(idx=None):
    if(idx == None):
        data = trumpTweetsTestData
    else:
        data = trumpTweetsTestData[int(idx)]
    return Response(json.dumps(data), mimetype="application/json")


@app.route("/user")
def user():
    '''
    User(user_id=1, first_name="Christian", last_name="Hur", 
        email="christian@uta.com", password="abc1234").save()
    User(user_id=2, first_name="Mary", last_name="Jane", 
        email="mary.jane@uta.com", password="password123").save()
    '''     
    users = User.objects.all()
    print('user count = ', len(users))
    return render_template("user.html", users=users)

@app.route("/news")
@app.route("/news/")
def news():
    print('get tweet count begin\n')
    tweets = trumpTweets
    print('tweet count = ', len(trumpTweets))
    return Response(json.dumps(trumpTweets), mimetype="application/json")
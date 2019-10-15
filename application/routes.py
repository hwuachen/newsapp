from application import app, db, english_bot
from flask import render_template, request, json, Response, redirect, flash
from trumptweets_testdata import trumpTweetsTestData
from application.models import User, Trumptweet
from application.forms import LoginForm, RegisterForm

trumpTweets = Trumptweet.objects.all()

def getDataItem(id, data):
    for dataItem in data:
        if id == dataItem['id_str']:
            return dataItem['id_str']

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", index=True)

@app.route("/chat")
def chat():
    return render_template("chat.html", chat=True)

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    bot_response = str(english_bot.get_response(userText))
    return bot_response

@app.route("/tweets/")
@app.route("/tweets/<year>")
def tweets(year="2018"):
    print(trumpTweets[0]["id_str"])
    '''passing data from source to view '''
    return render_template("tweet.html", dataList=trumpTweets, tweet=True, year=year, total=len(trumpTweets))


@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # if request.form.get("email") == "test@credit-suisse.com":
        #     print ("email: =", request.form.get("email") )
        #     # flask message will only set on time on browser. Net to set common in layout 
        #     flash("You are successfully logged in!", "success")
        email       = form.email.data
        password    = form.password.data        
        user = User.objects(email=email).first()

        print('email =', email)
        print('password =', password)
        print('user.password =', user.password)            

        #if user and password == user.password:
        if user and user.get_password(password):
            flash(f"{user.first_name}, you are successfully logged in!", "success")
            return redirect("/index")
        else:
            flash("Sorry, something went wrong.","danger")
    return render_template("login.html", title="Login", form=form, login=True )


@app.route("/register", methods=['POST','GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_id     = User.objects.count()
        user_id     += 1

        email       = form.email.data
        password    = form.password.data
        first_name  = form.first_name.data
        last_name   = form.last_name.data

        user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        flash("You are successfully registered!","success")
        return redirect(url_for('index'))
    return render_template("register.html", title="Register", form=form, register=True)


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
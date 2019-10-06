# Installation
## Python (latest include pip)
https://www.python.org/downloads/
>python -v
>py 
## pip - Python package manager
>pip --version
if not installed, follow https://pip.pypa.io/en/stable/installing/
>pip list
>pip install or uninstall
## the virtual env
>pip install virtualenv

## create virtual env
py -m venv venv1
venv1\Scripts\activate

## flask 
>pip install flask

## flask-wtf  form modules

## python-dotenv  - to enable env variables in .flaskenv

add below to .flaskenv
FLASK_ENV=development
FLASK_APP=main.py

## create requirement.txt
pip freeze > requirements.txt
pip install -r requirements.txt

## flask - run      --to run

### MongoDB 
### flask-mongoengine  -- MongoEngine extension for Flask, come with wtf friendly data types

if can not connect to Mongo. This happened probably because the MongoDB service isn't started. Follow the below steps to start it:

Go to Control Panel and click on Administrative Tools.
Double click on Services. A new window opens up.
Search MongoDB.exe. Right click on it and select Start.

#### import data 
>mongoimport --jsonArray --db News --collection trumptweet --file C:\Users\Chen\Documents\MyCode\trump_tweet_data_archive-master\2018.json

Failed: error processing document #1: invalid character 'o' in literal NaN or Number (expecting 'a' or 'u')
solved by --jsonArray 

#### why pymongo vs mongoengine
https://stackoverflow.com/questions/5712857/pymongo-vs-mongoengine-for-django

<MonggoDB> 
- create collections to store documents (data)
- insert documents into collections
- using MongoDB shell 
	db.createCollection(<collection>)
	db.<collection>.insert({...})
	db.<collection>.insertMany({...})
- insert JSON file /data directly using mongoimport.exe via commandline
	mongoimport --db <DB> --collection <collection> --file <file>
	mongoimport --d <DB> -c <collection> --file <file>  --jsonArray    //with shortcut

#### Git 
Git:  git --version
Git init // init local git repository
Git add //add file to index
Git status // check statics of a working tree
Git commit // commit changes in index
Git push //push to repository
Git pull // pull attest from remote repository
Git clone // clone to a new repository
Git rm –cache index.html //before commit can delete
Git commit 
Click “I” to edit. 
>git clone https://github.com/hwuachen/git-trump-tweets.git
>git status 
> git  add .
> git commit -m “message to comment”
> git push https://github.com/hwuachen/git-trump-tweets.git
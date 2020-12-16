from flask import Flask, render_template
import pymongo
from pymongo import MongoClient

app = Flask(__name__)



#connecting to the database
client = pymongo.MongoClient('localhost', 27017)
#client = pymongo.MongoClient('mongodb+srv://root:Shaytards123@cluster0.szmco.mongodb.net/Software_Project?retryWrites=true&w=majority')
db = client.login_system


# user routes
from user import routes



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/shinder")
def shinder():
    return render_template("main.html")

@app.route("/review")
def blog():
    return render_template("review.html")

@app.route("/forum")
def forum():
    return render_template("forum.html")

if __name__ == "__main__":
    app.debug = True
    app.run()


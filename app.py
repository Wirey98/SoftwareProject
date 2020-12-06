from flask import Flask, render_template
import pymongo
app = Flask(__name__)

#connecting to the database
client = pymongo.MongoClient('localhost', 27017)
db = client.login_system

# user routes
from user import routes



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/shinder")
def shinder():
    return render_template("main.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/forum")
def forum():
    return render_template("forum.html")

if __name__ == "__main__":
    app.run()


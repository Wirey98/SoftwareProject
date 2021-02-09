from flask import Flask, render_template, session, redirect, request
from functools import wraps
import pymongo
import folium
import requests
from pymongo import MongoClient

app = Flask(__name__)

app.secret_key = 'hajhaauopqsbyuajc'

#connecting to the database
cluster = MongoClient('mongodb+srv://root:Shaytards123@cluster0.szmco.mongodb.net/Software_Project?retryWrites=true&w=majority')


database1 = cluster["Software_Project"]
collection = database1["users"]

#collection.insert_one({"id":0, "seed_name":"onions"})

#client = pymongo.MongoClient('mongodb+srv://root:Shaytards123@cluster0.szmco.mongodb.net/Software_Project?retryWrites=true&w=majority')
#databasefirst = client.login_system

#app.config['databaseURI'] = 'mongodb+srv://root:Shaytards123@cluster0.szmco.mongodb.net/Software_Project?retryWrites=true&w=majority'
#app.config[]

# Decorators
def login_manditory(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'Logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap


# user routes
from user import routes


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/shinder")
@login_manditory
def shinder():
    return render_template("main.html")

@app.route("/review")
@login_manditory
def blog():
    return render_template("review.html")

@app.route("/forum")
@login_manditory
def forum():
    return render_template("forum.html")

@app.route("/homepage")
@login_manditory
def homepage():
    return render_template("homepage.html")

@app.route("/homescreen")
@login_manditory
def homescreen():
    return render_template("homescreen.html")

#@app.route("/APIsearch")
#@login_manditory
#def shoesearch():
 #   return render_template("shoesearch.html")

#@app.route("/apiresult", methods=["POST"])
#@login_manditory
#def apiresult():
    #getting the form value
    #shoes = request.form['shoe']
 #   r = requests.get('')
  #  json_object = r.text
   # return json_object
    #return render_template("apiresult.html")


@app.route("/maptest")
@login_manditory
def map():
    map = folium.Map(
        location=[53.3379897, -6.259073],
        tiles='Stamen Terrain',
        zoom_start=17
    )

    folium.Circle([53.3379897, -6.259073],
    radius=200).add_to(map)

    return map._repr_html_()


if __name__ == "__main__":
    app.debug = True
    app.run()


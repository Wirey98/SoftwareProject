from flask import Flask, render_template, session, redirect, request
from functools import wraps
import pymongo
import folium
import requests
import json
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

@app.route("/APIsearch")
@login_manditory
def shoesearch():
    return render_template("shoesearch.html")

   

@app.route("/apiresult", methods=["POST"])
@login_manditory
def apiresult():
    #getting the form value
    brandname = request.form['brand']
    gendertype = request.form['gender']
    r = requests.get('https://api.thesneakerdatabase.com/v1/sneakers?limit=100&brand='+brandname+'&gender='+gendertype)
    #json_object = json.loads(r['results'])
    json_object = r.json()


    #for key in json_object:
        #print (key, ":", json_object[key])
        
        
        # json_object['results'][i]['shoe']
    
    #sneaker 1 
    name_result = json_object['results'][0]['name']
    shoe_result = json_object['results'][0]['media']['imageUrl']
    price_result = json_object['results'][0]['retailPrice']
    #sneaker 2
    name_result2 = json_object['results'][1]['name']
    shoe_result2 = json_object['results'][1]['media']['imageUrl']
    price_result2 = json_object['results'][1]['retailPrice']

    #sneaker 3
    name_result3 = json_object['results'][2]['name']
    shoe_result3 = json_object['results'][2]['media']['imageUrl']
    price_result3 = json_object['results'][2]['retailPrice']

    #sneaker 4
    name_result4 = json_object['results'][3]['name']
    shoe_result4 = json_object['results'][3]['media']['imageUrl']
    price_result4 = json_object['results'][3]['retailPrice']

    #sneaker 5
    name_result5 = json_object['results'][4]['name']
    shoe_result5 = json_object['results'][4]['media']['imageUrl']
    price_result5 = json_object['results'][4]['retailPrice']

    #return shoe_result
    return render_template('shoesearch.html', 
    imageUrl=shoe_result, name=name_result, price=price_result,
    imageUrl2=shoe_result2, name2=name_result2,price1=price_result2,
    imageUrl3=shoe_result3, name3=name_result3,price2=price_result3,
    imageUrl4=shoe_result4, name4=name_result4,price3=price_result4,
    imageUrl5=shoe_result5, name5=name_result5,price4=price_result5)


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


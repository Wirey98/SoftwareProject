from flask import Flask, render_template, session, redirect, request
from functools import wraps
import pymongo
import folium
import requests
import json
from pymongo import MongoClient
from pprint import pprint


app = Flask(__name__)

app.secret_key = 'hajhaauopqsbyuajc'

#connecting to the database
cluster = MongoClient('mongodb+srv://root:Shaytards123@cluster0.szmco.mongodb.net/Software_Project?retryWrites=true&w=majority')


database1 = cluster["Software_Project"]
collection = database1["users"]

database2 = cluster["Software_Project"]
collection1 = database2["forumCluster"]
collection2 = database2["forums"]


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
    return render_template("forum.html", collectiontest=collection2)

@app.route("/homepage")
@login_manditory
def homepage():
    return render_template("homepage.html")

@app.route("/homescreen")
@login_manditory
def homescreen():
    return render_template("homescreen.html")

@app.route("/APIsearch")

def shoesearch():
    return render_template("shoesearch.html")

@app.route("/forumResult")

def forumResult():
    return render_template('forumResult.html', collectiontest=collection2)
    
   # for x in collection1.find({}, {"_id":0, "forumName": 1, "forumTitle": 1, "forumPost": 1 }):
      #  return render_template("forumResult.html",x)

        
    

   

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
    color_result = json_object['results'][0]['colorway']
    
    #sneaker 2
    name_result2 = json_object['results'][1]['name']
    shoe_result2 = json_object['results'][1]['media']['imageUrl']
    color_result2 = json_object['results'][1]['colorway']

    #sneaker 3
    name_result3 = json_object['results'][2]['name']
    shoe_result3 = json_object['results'][2]['media']['imageUrl']
    color_result3 = json_object['results'][2]['colorway']

    #sneaker 4
    name_result4 = json_object['results'][3]['name']
    shoe_result4 = json_object['results'][3]['media']['imageUrl']
    color_result4 = json_object['results'][3]['colorway']

    #sneaker 5
    name_result5 = json_object['results'][4]['name']
    shoe_result5 = json_object['results'][4]['media']['imageUrl']
    color_result5 = json_object['results'][4]['colorway']
    
    #sneaker 6
    name_result6 = json_object['results'][5]['name']
    shoe_result6 = json_object['results'][5]['media']['imageUrl']
    color_result6 = json_object['results'][5]['colorway']
    
    #sneaker 7
    name_result7 = json_object['results'][6]['name']
    shoe_result7 = json_object['results'][6]['media']['imageUrl']
    color_result7 = json_object['results'][6]['colorway']

    #sneaker 8
    name_result8 = json_object['results'][7]['name']
    shoe_result8 = json_object['results'][7]['media']['imageUrl']
    color_result8 = json_object['results'][7]['colorway']

    #sneaker 9
    name_result9 = json_object['results'][8]['name']
    shoe_result9 = json_object['results'][8]['media']['imageUrl']
    color_result9 = json_object['results'][8]['colorway']

    #sneaker 10
    name_result10 = json_object['results'][9]['name']
    shoe_result10 = json_object['results'][9]['media']['imageUrl']
    color_result10 = json_object['results'][9]['colorway']

    #sneaker 11
    name_result11 = json_object['results'][10]['name']
    shoe_result11 = json_object['results'][10]['media']['imageUrl']
    color_result11 = json_object['results'][10]['colorway']

    #sneaker 12
    name_result12 = json_object['results'][11]['name']
    shoe_result12 = json_object['results'][11]['media']['imageUrl']
    color_result12 = json_object['results'][11]['colorway']

    #sneaker 13
    name_result13 = json_object['results'][12]['name']
    shoe_result13 = json_object['results'][12]['media']['imageUrl']
    color_result13 = json_object['results'][12]['colorway']

    #sneaker 14
    name_result14 = json_object['results'][13]['name']
    shoe_result14 = json_object['results'][13]['media']['imageUrl']
    color_result14 = json_object['results'][13]['colorway']

    #sneaker 15
    name_result15 = json_object['results'][14]['name']
    shoe_result15 = json_object['results'][14]['media']['imageUrl']
    color_result15 = json_object['results'][14]['colorway']

    #sneaker 16
    name_result16 = json_object['results'][15]['name']
    shoe_result16 = json_object['results'][15]['media']['imageUrl']
    color_result16 = json_object['results'][15]['colorway']

    #sneaker 17
    name_result17 = json_object['results'][16]['name']
    shoe_result17 = json_object['results'][16]['media']['imageUrl']
    color_result17 = json_object['results'][16]['colorway']

    #sneaker 18
    name_result18 = json_object['results'][17]['name']
    shoe_result18 = json_object['results'][17]['media']['imageUrl']
    color_result18 = json_object['results'][17]['colorway']

    #sneaker 19
    name_result19 = json_object['results'][18]['name']
    shoe_result19 = json_object['results'][18]['media']['imageUrl']
    color_result19 = json_object['results'][18]['colorway']

    #sneaker 20
    name_result20 = json_object['results'][19]['name']
    shoe_result20 = json_object['results'][19]['media']['imageUrl']
    color_result20 = json_object['results'][19]['colorway']

    

    #return shoe_result
    return render_template('apiresult.html', 
    imageUrl=shoe_result, name=name_result, color=color_result,
    imageUrl2=shoe_result2, name2=name_result2,color2=color_result2,
    imageUrl3=shoe_result3, name3=name_result3,color3=color_result3,
    imageUrl4=shoe_result4, name4=name_result4,color4=color_result4,
    imageUrl5=shoe_result5, name5=name_result5,color5=color_result5,
    imageUrl6=shoe_result6, name6=name_result6,color6=color_result6,
    imageUrl7=shoe_result7, name7=name_result7,color7=color_result7,
    imageUrl8=shoe_result8, name8=name_result8,color8=color_result8,
    imageUrl9=shoe_result9, name9=name_result9,color9=color_result9,
    imageUrl10=shoe_result10, name10=name_result10,color10=color_result10,
    imageUrl11=shoe_result11, name11=name_result11,color11=color_result11,
    imageUrl12=shoe_result12, name12=name_result12,color12=color_result12,
    imageUrl13=shoe_result13, name13=name_result13,color13=color_result13,
    imageUrl14=shoe_result14, name14=name_result14,color14=color_result14,
    imageUrl15=shoe_result15, name15=name_result15,color15=color_result15,
    imageUrl16=shoe_result16, name16=name_result16,color16=color_result16,
    imageUrl17=shoe_result17, name17=name_result17,color17=color_result17,
    imageUrl18=shoe_result18, name18=name_result18,color18=color_result18,
    imageUrl19=shoe_result19, name19=name_result19,color19=color_result19,
    imageUrl20=shoe_result20, name20=name_result20,color20=color_result20,)


   

    

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


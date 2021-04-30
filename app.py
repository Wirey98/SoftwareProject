from flask import Flask, render_template, session, redirect, request
from functools import wraps
import pymongo
import folium
import requests
import json
import logging
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
@login_manditory
def shoesearch():
    return render_template("shoesearch.html")

@app.route("/forumResult")
@login_manditory
def forumResult():
    return render_template('forumResult.html', collectiontest=collection2)
    
   # for x in collection1.find({}, {"_id":0, "forumName": 1, "forumTitle": 1, "forumPost": 1 }):
      #  return render_template("forumResult.html",x)

        
@app.route("/newapi", methods=["GET","POST"])

def newapi():

    
    url = 'https://v1-sneakers.p.rapidapi.com/v1/sneakers'

    
    brandname1 = request.form.get('brand')
    gendertype1 = request.form.get('gender')
    
    #str(brandname1)
    #str(gendertype1)
    

    querystring = {"limit":"100", "brand":brandname1, "gender":gendertype1}
    
    headers = {
    'x-rapidapi-key': "8b43fcfb00mshdc3d24bd007747ap16b617jsn324bb8a411e2",
    'x-rapidapi-host': "v1-sneakers.p.rapidapi.com"
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    

    json_object = response.json()
    

    
    

    #sneaker 1 
    name_result = json_object['results'][0]['name']
    shoe_result = json_object['results'][0]['media']['imageUrl']
    color_result = json_object['results'][0]['colorway']
    releaseDate_result = json_object['results'][0]['releaseDate']
    
    #sneaker 2
    name_result2 = json_object['results'][1]['name']
    shoe_result2 = json_object['results'][1]['media']['imageUrl']
    color_result2 = json_object['results'][1]['colorway']
    releaseDate_result2 = json_object['results'][1]['releaseDate']

    #sneaker 3
    name_result3 = json_object['results'][2]['name']
    shoe_result3 = json_object['results'][2]['media']['imageUrl']
    color_result3 = json_object['results'][2]['colorway']
    releaseDate_result3 = json_object['results'][2]['releaseDate']

    #sneaker 4
    name_result4 = json_object['results'][3]['name']
    shoe_result4 = json_object['results'][3]['media']['imageUrl']
    color_result4 = json_object['results'][3]['colorway']
    releaseDate_result4 = json_object['results'][3]['releaseDate']

    #sneaker 5
    name_result5 = json_object['results'][4]['name']
    shoe_result5 = json_object['results'][4]['media']['imageUrl']
    color_result5 = json_object['results'][4]['colorway']
    releaseDate_result5 = json_object['results'][4]['releaseDate']
    
    #sneaker 6
    name_result6 = json_object['results'][5]['name']
    shoe_result6 = json_object['results'][5]['media']['imageUrl']
    color_result6 = json_object['results'][5]['colorway']
    releaseDate_result6 = json_object['results'][5]['releaseDate']
    
    #sneaker 7
    name_result7 = json_object['results'][6]['name']
    shoe_result7 = json_object['results'][6]['media']['imageUrl']
    color_result7 = json_object['results'][6]['colorway']
    releaseDate_result7 = json_object['results'][6]['releaseDate']

    #sneaker 8
    name_result8 = json_object['results'][7]['name']
    shoe_result8 = json_object['results'][7]['media']['imageUrl']
    color_result8 = json_object['results'][7]['colorway']
    releaseDate_result8 = json_object['results'][7]['releaseDate']

    #sneaker 9
    name_result9 = json_object['results'][8]['name']
    shoe_result9 = json_object['results'][8]['media']['imageUrl']
    color_result9 = json_object['results'][8]['colorway']
    releaseDate_result9 = json_object['results'][8]['releaseDate']

    #sneaker 10
    name_result10 = json_object['results'][9]['name']
    shoe_result10 = json_object['results'][9]['media']['imageUrl']
    color_result10 = json_object['results'][9]['colorway']
    releaseDate_result10 = json_object['results'][9]['releaseDate']

    #sneaker 11
    name_result11 = json_object['results'][10]['name']
    shoe_result11 = json_object['results'][10]['media']['imageUrl']
    color_result11 = json_object['results'][10]['colorway']
    releaseDate_result11 = json_object['results'][10]['releaseDate']

    #sneaker 12
    name_result12 = json_object['results'][11]['name']
    shoe_result12 = json_object['results'][11]['media']['imageUrl']
    color_result12 = json_object['results'][11]['colorway']
    releaseDate_result12 = json_object['results'][11]['releaseDate']

    #sneaker 13
    name_result13 = json_object['results'][12]['name']
    shoe_result13 = json_object['results'][12]['media']['imageUrl']
    color_result13 = json_object['results'][12]['colorway']
    releaseDate_result13 = json_object['results'][12]['releaseDate']

    #sneaker 14
    name_result14 = json_object['results'][13]['name']
    shoe_result14 = json_object['results'][13]['media']['imageUrl']
    color_result14 = json_object['results'][13]['colorway']
    releaseDate_result14 = json_object['results'][13]['releaseDate']

    #sneaker 15
    name_result15 = json_object['results'][14]['name']
    shoe_result15 = json_object['results'][14]['media']['imageUrl']
    color_result15 = json_object['results'][14]['colorway']
    releaseDate_result15 = json_object['results'][14]['releaseDate']

    #sneaker 16
    name_result16 = json_object['results'][15]['name']
    shoe_result16 = json_object['results'][15]['media']['imageUrl']
    color_result16 = json_object['results'][15]['colorway']
    releaseDate_result16 = json_object['results'][15]['releaseDate']

    #sneaker 17
    name_result17 = json_object['results'][16]['name']
    shoe_result17 = json_object['results'][16]['media']['imageUrl']
    color_result17 = json_object['results'][16]['colorway']
    releaseDate_result17 = json_object['results'][16]['releaseDate']

    #sneaker 18
    name_result18 = json_object['results'][17]['name']
    shoe_result18 = json_object['results'][17]['media']['imageUrl']
    color_result18 = json_object['results'][17]['colorway']
    releaseDate_result18 = json_object['results'][17]['releaseDate']

    #sneaker 19
    name_result19 = json_object['results'][18]['name']
    shoe_result19 = json_object['results'][18]['media']['imageUrl']
    color_result19 = json_object['results'][18]['colorway']
    releaseDate_result19 = json_object['results'][18]['releaseDate']

    #sneaker 20
    name_result20 = json_object['results'][19]['name']
    shoe_result20 = json_object['results'][19]['media']['imageUrl']
    color_result20 = json_object['results'][19]['colorway']
    releaseDate_result20 = json_object['results'][19]['releaseDate']

    #sneaker 21
    name_result21 = json_object['results'][20]['name']
    shoe_result21 = json_object['results'][20]['media']['imageUrl']
    color_result21 = json_object['results'][20]['colorway']
    releaseDate_result21 = json_object['results'][20]['releaseDate']

    #sneaker 22
    name_result22 = json_object['results'][21]['name']
    shoe_result22 = json_object['results'][21]['media']['imageUrl']
    color_result22 = json_object['results'][21]['colorway']
    releaseDate_result22 = json_object['results'][21]['releaseDate']

    #sneaker 23
    name_result23 = json_object['results'][22]['name']
    shoe_result23 = json_object['results'][22]['media']['imageUrl']
    color_result23 = json_object['results'][22]['colorway']
    releaseDate_result23 = json_object['results'][22]['releaseDate']

    #sneaker 24
    name_result24 = json_object['results'][23]['name']
    shoe_result24 = json_object['results'][23]['media']['imageUrl']
    color_result24 = json_object['results'][23]['colorway']
    releaseDate_result24 = json_object['results'][23]['releaseDate']

    #sneaker 25
    name_result25 = json_object['results'][24]['name']
    shoe_result25 = json_object['results'][24]['media']['imageUrl']
    color_result25 = json_object['results'][24]['colorway']
    releaseDate_result25 = json_object['results'][24]['releaseDate']

    #sneaker 26
    name_result26 = json_object['results'][25]['name']
    shoe_result26 = json_object['results'][25]['media']['imageUrl']
    color_result26 = json_object['results'][25]['colorway']
    releaseDate_result26 = json_object['results'][25]['releaseDate']

    #sneaker 27
    name_result27 = json_object['results'][26]['name']
    shoe_result27 = json_object['results'][26]['media']['imageUrl']
    color_result27 = json_object['results'][26]['colorway']
    releaseDate_result27 = json_object['results'][26]['releaseDate']

    #sneaker 28
    name_result28 = json_object['results'][27]['name']
    shoe_result28 = json_object['results'][27]['media']['imageUrl']
    color_result28 = json_object['results'][27]['colorway']
    releaseDate_result28 = json_object['results'][27]['releaseDate']

    #sneaker 29
    name_result29 = json_object['results'][28]['name']
    shoe_result29 = json_object['results'][28]['media']['imageUrl']
    color_result29 = json_object['results'][28]['colorway']
    releaseDate_result29 = json_object['results'][28]['releaseDate']

    #sneaker 30
    name_result30 = json_object['results'][29]['name']
    shoe_result30 = json_object['results'][29]['media']['imageUrl']
    color_result30 = json_object['results'][29]['colorway']
    releaseDate_result30 = json_object['results'][29]['releaseDate']

    #sneaker 31
    name_result31 = json_object['results'][30]['name']
    shoe_result31 = json_object['results'][30]['media']['imageUrl']
    color_result31 = json_object['results'][30]['colorway']
    releaseDate_result31 = json_object['results'][30]['releaseDate']

    #sneaker 32
    name_result32 = json_object['results'][31]['name']
    shoe_result32 = json_object['results'][31]['media']['imageUrl']
    color_result32 = json_object['results'][31]['colorway']
    releaseDate_result32 = json_object['results'][31]['releaseDate']

    #sneaker 33
    name_result33 = json_object['results'][32]['name']
    shoe_result33 = json_object['results'][32]['media']['imageUrl']
    color_result33 = json_object['results'][32]['colorway']
    releaseDate_result33 = json_object['results'][32]['releaseDate']

    #sneaker 34
    name_result34 = json_object['results'][33]['name']
    shoe_result34 = json_object['results'][33]['media']['imageUrl']
    color_result34 = json_object['results'][33]['colorway']
    releaseDate_result34 = json_object['results'][33]['releaseDate']

    #sneaker 35
    name_result35 = json_object['results'][34]['name']
    shoe_result35 = json_object['results'][34]['media']['imageUrl']
    color_result35 = json_object['results'][34]['colorway']
    releaseDate_result35 = json_object['results'][34]['releaseDate']

    #sneaker 36
    name_result36 = json_object['results'][35]['name']
    shoe_result36 = json_object['results'][35]['media']['imageUrl']
    color_result36 = json_object['results'][35]['colorway']
    releaseDate_result36 = json_object['results'][35]['releaseDate']

    #sneaker 37
    name_result37 = json_object['results'][36]['name']
    shoe_result37 = json_object['results'][36]['media']['imageUrl']
    color_result37 = json_object['results'][36]['colorway']
    releaseDate_result37 = json_object['results'][36]['releaseDate']

    #sneaker 38
    name_result38 = json_object['results'][37]['name']
    shoe_result38 = json_object['results'][37]['media']['imageUrl']
    color_result38 = json_object['results'][37]['colorway']
    releaseDate_result38 = json_object['results'][37]['releaseDate']

    #sneaker 39
    name_result39 = json_object['results'][38]['name']
    shoe_result39 = json_object['results'][38]['media']['imageUrl']
    color_result39 = json_object['results'][38]['colorway']
    releaseDate_result39 = json_object['results'][38]['releaseDate']


    

    #return shoe_result
    return render_template('newapi.html', 
    imageUrl=shoe_result, name=name_result, color=color_result, releaseDate=releaseDate_result,
    imageUrl2=shoe_result2, name2=name_result2,color2=color_result2,releaseDate2=releaseDate_result2,
    imageUrl3=shoe_result3, name3=name_result3,color3=color_result3,releaseDate3=releaseDate_result3,
    imageUrl4=shoe_result4, name4=name_result4,color4=color_result4,releaseDate4=releaseDate_result4,
    imageUrl5=shoe_result5, name5=name_result5,color5=color_result5,releaseDate5=releaseDate_result5,
    imageUrl6=shoe_result6, name6=name_result6,color6=color_result6,releaseDate6=releaseDate_result6,
    imageUrl7=shoe_result7, name7=name_result7,color7=color_result7,releaseDate7=releaseDate_result7,
    imageUrl8=shoe_result8, name8=name_result8,color8=color_result8,releaseDate8=releaseDate_result8,
    imageUrl9=shoe_result9, name9=name_result9,color9=color_result9,releaseDate9=releaseDate_result9,
    imageUrl10=shoe_result10, name10=name_result10,color10=color_result10,releaseDate10=releaseDate_result10,
    imageUrl11=shoe_result11, name11=name_result11,color11=color_result11,releaseDate11=releaseDate_result11,
    imageUrl12=shoe_result12, name12=name_result12,color12=color_result12,releaseDate12=releaseDate_result12,
    imageUrl13=shoe_result13, name13=name_result13,color13=color_result13,releaseDate13=releaseDate_result13,
    imageUrl14=shoe_result14, name14=name_result14,color14=color_result14,releaseDate14=releaseDate_result14,
    imageUrl15=shoe_result15, name15=name_result15,color15=color_result15,releaseDate15=releaseDate_result15,
    imageUrl16=shoe_result16, name16=name_result16,color16=color_result16,releaseDate16=releaseDate_result16,
    imageUrl17=shoe_result17, name17=name_result17,color17=color_result17,releaseDate17=releaseDate_result17,
    imageUrl18=shoe_result18, name18=name_result18,color18=color_result18,releaseDate18=releaseDate_result18,
    imageUrl19=shoe_result19, name19=name_result19,color19=color_result19,releaseDate19=releaseDate_result19,
    imageUrl20=shoe_result20, name20=name_result20,color20=color_result20,releaseDate20=releaseDate_result20,
    imageUrl21=shoe_result21, name21=name_result21, color21=color_result21, releaseDate21=releaseDate_result21,
    imageUrl22=shoe_result22, name22=name_result22, color22=color_result22, releaseDate22=releaseDate_result22,
    imageUrl23=shoe_result23, name23=name_result23, color23=color_result23, releaseDate23=releaseDate_result23,
    imageUrl24=shoe_result24, name24=name_result24, color24=color_result24, releaseDate24=releaseDate_result24,
    imageUrl25=shoe_result25, name25=name_result25, color25=color_result25, releaseDate25=releaseDate_result25,
    imageUrl26=shoe_result26, name26=name_result26, color26=color_result26, releaseDate26=releaseDate_result26,
    imageUrl27=shoe_result27, name27=name_result27, color27=color_result27, releaseDate27=releaseDate_result27,
    imageUrl28=shoe_result28, name28=name_result28, color28=color_result28, releaseDate28=releaseDate_result28,
    imageUrl29=shoe_result29, name29=name_result29, color29=color_result29, releaseDate29=releaseDate_result29,
    imageUrl30=shoe_result30, name30=name_result30, color30=color_result30, releaseDate30=releaseDate_result30,
    imageUrl31=shoe_result31, name31=name_result31, color31=color_result31, releaseDate31=releaseDate_result31,
    imageUrl32=shoe_result32, name32=name_result32, color32=color_result32, releaseDate32=releaseDate_result32,
    imageUrl33=shoe_result33, name33=name_result33, color33=color_result33, releaseDate33=releaseDate_result33,
    imageUrl34=shoe_result34, name34=name_result34, color34=color_result34, releaseDate34=releaseDate_result34,
    imageUrl35=shoe_result35, name35=name_result35, color35=color_result35, releaseDate35=releaseDate_result35,
    imageUrl36=shoe_result36, name36=name_result36, color36=color_result36, releaseDate36=releaseDate_result36,
    imageUrl37=shoe_result37, name37=name_result37, color37=color_result37, releaseDate37=releaseDate_result37,
    imageUrl38=shoe_result38, name38=name_result38, color38=color_result38, releaseDate38=releaseDate_result38,
    imageUrl39=shoe_result39, name39=name_result39, color39=color_result39, releaseDate39=releaseDate_result39)


   

    

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


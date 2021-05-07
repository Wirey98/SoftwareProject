#ClassName: models.py
#  Date: 04/05/2021
#@author Sam Greenan, x17449342
#
#@reference 
# https://www.youtube.com/watch?v=w1STSSumoVk - Login routes


from flask import Flask

#from the app file, import the instance of Flask
from app import app

from user.models import User

from forum.forumModels import Forum

@app.route('/user/signup', methods =['POST'])
def signup():
    return User().signup()

@app.route('/user/signout')
def signout():
    return User().signout()

@app.route('/user/login', methods =['POST'])
def login():
    return User().login()

@app.route('/forum/post', methods=['POST'])
def posting():
    return Forum().forumPost()
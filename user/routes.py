from flask import Flask

#from the app file, import the instance of Flask
from app import app

from user.models import User

@app.route('/user/signup', methods =['GET'])
def signup():
    return User().signup()

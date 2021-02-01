from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from app import database1
import uuid


class User:

    def session1(self, user):
        del user['password']
        session['Logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self):
        print(request.form)

        #creating the specific user
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        # encryption
        user['password'] = pbkdf2_sha256.encrypt(user['password'])


        #removing duplicates to check whether the email address already exists
        if database1.users.find_one({"email": user['email'] }):
            return jsonify({"error": "Email entered already has an account"}), 400


        if database1.users.insert_one(user):
            return self.session1(user)

        

        return jsonify({"error": "Signup has failed" }), 400 

    #sign out method
    def signout(self):
        session.clear()
        return redirect('/')

    #sign in method
    def login(self):

        user = database1.users.find_one({
            "email": request.form.get('email')
        })

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.session1(user)

        return jsonify({ "error": "Login has failed, Email or Password is incorrect" }), 401


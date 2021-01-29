from flask import Flask, jsonify, request
from passlib.hash import pbkdf2_sha256
from app import database1
import uuid


class User:

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


        #removing duplicates
        if database1.users.find_one({"email": user['email'] }):
            return jsonify({"error": "Email entered already has an account"}), 400


        database1.users.insert_one(user)

        

        return jsonify(user), 200 

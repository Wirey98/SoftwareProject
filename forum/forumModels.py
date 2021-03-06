from flask import Flask, jsonify, request, session
from datetime import datetime
import uuid
import time
from app import database2
from app import database1


class Forum:


    def forumPost(self):
        #creation of the forum post object
        forum = {
            "_id": uuid.uuid4().hex,
            "forumName": session['user']['name'],
            "forumTitle": request.form.get('forumTitle'),
            "forumPost": request.form.get('forumPost'),
            "forumTime": datetime.now(),
            "forumImage": request.form.get('forumImage')
        }

        if database2.forums.insert_one(forum):
            return jsonify(forum), 200

        return jsonify({"error": "failed"}), 400
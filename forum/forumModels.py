from flask import Flask, jsonify, request, session
import uuid
from app import database2
class Forum:

    def session_init(self, forum):
        session['forum'] = forum
        return jsonify(forum), 200

    def forumPost(self):
        #creation of the forum post object
        forum = {
            "_id": uuid.uuid4().hex,
            "forumName": request.form.get('forumName'),
            "forumTitle": request.form.get('forumTitle'),
            "forumPost": request.form.get('forumPost')

        }

        if database2.forums.insert_one(forum):
            return self.session_init(forum)

        return jsonify(forum), 200
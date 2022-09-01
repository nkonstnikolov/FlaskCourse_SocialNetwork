from flask_restful import Resource
from flask import request
from managers.auth import auth
from managers.message import MessageManager, InboxManager

class SendMessageResource(Resource):

    @auth.login_required
    def post(self):
        data = request.get_json()
        message = MessageManager.create_message(data["sender_id"],
                                                data["recipient_id"],
                                                data["message"])
        return {"message": "Message sent"}, 201
        
class InboxResource(Resource):
    
    @auth.login_required
    def get(self):
        data = request.get_json()
        user_id = data["user_id"]
        messages = InboxManager.inbox(user_id)
        
        return {"messages": [message.serialize() for message in messages]}, 200
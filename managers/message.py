from werkzeug.exceptions import NotFound, BadRequest
from models.message import MessageModel
from models.user import UserModel
from db import db


class MessageManager:

    @staticmethod
    def create_message(sender_id, recipient_id, message):
    
        sender = UserModel.query.filter_by(user_id=sender_id).first()
        recipient = UserModel.query.filter_by(user_id=recipient_id).first()
        if not recipient:
            raise BadRequest("Recipient does not exist")

        message = MessageModel(sender_id=sender_id,
                               recipient_id=recipient_id, message=message)
        db.session.add(message)
        db.session.commit()

        return message


class InboxManager:

    @staticmethod
    def inbox(user_id):
    
        messages = MessageModel.query.filter_by(recipient_id=user_id).all()

        if not messages:
            raise NotFound("No messages found")

        return messages
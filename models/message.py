from sqlalchemy import func
from db import db
from models.user import UserModel


class MessageModel(db.Model):
    __tablename__ = "message"

    message_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    sender = db.relationship("UserModel", foreign_keys=[sender_id])
    recipient = db.relationship("UserModel", foreign_keys=[recipient_id])
    message = db.Column(db.Text, nullable=False)
    created_datetime = db.Column(db.DateTime, server_default=func.now())
    
    def serialize(self):
        return {
            "sender_id": self.sender_id,
            "recipient_id": self.recipient_id,
            "message": self.message
            }
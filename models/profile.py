from sqlalchemy import func
from db import db
from models.user import UserModel


class ProfileModel(db.Model):
    """ Profile Model for storing user profile details """
    __tablename__ = "profile"

    profile_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    user = db.relationship("UserModel")
    age = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(50), nullable=True)
    sex = db.Column(db.Enum("Male", "Female", "Other"), nullable=False)
    school = db.Column(db.String(100), nullable=True)
    created_datetime = db.Column(db.DateTime, server_default=func.now())
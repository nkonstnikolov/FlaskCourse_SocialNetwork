from sqlalchemy import func
from db import db
from models.enums import UserRole


class UserModel(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    created_datetime = db.Column(db.DateTime, server_default=func.now())
    user_role = db.Column(db.Enum(UserRole), nullable=False)
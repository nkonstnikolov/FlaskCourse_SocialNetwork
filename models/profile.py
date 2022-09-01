from sqlalchemy import func
from db import db
from models.user import UserModel


class ProfileModel(db.Model):
    """ Profile Model for storing user profile details """
    __tablename__ = "profile"

    profile_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), unique=True, nullable=False)
    user = db.relationship("UserModel")
    age = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(50), nullable=True)
    sex = db.Column(db.Enum("Male", "Female", "Other", name="gender"), nullable=False)
    school = db.Column(db.String(100), nullable=True)
    created_datetime = db.Column(db.DateTime, server_default=func.now())
    
    def serialize(self):
        return {
            "profile_id": self.profile_id,
            "user_id": self.user_id,
            "age": self.age,
            "location": self.location,
            "sex": self.sex,
            "school": self.school,
            "created_datetime": str(self.created_datetime)
        }
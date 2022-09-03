from werkzeug.exceptions import NotFound, BadRequest
from models.profile import ProfileModel
from models.user import UserModel
from db import db


class ProfileManager:

    @staticmethod
    def create_profile(data):
        user = UserModel.query.filter_by(user_id=UserModel.user_id).first()
        if not user:
            raise BadRequest("User does not exist")

        profile = ProfileModel(**data)
        db.session.add(profile)
        db.session.commit()

        return profile


    @staticmethod
    def edit_profile(data):
        user = UserModel.query.filter_by(user_id=UserModel.user_id).first()
        if not user:
            raise BadRequest("User does not exist")

        profile = ProfileModel(**data)
        
        if data.get("age"):
            profile.age = data["age"]
        if data.get("location"):
            profile.location = data["location"]
        if data.get("sex"):
            profile.sex = data["sex"]
        if data.get("school"):
            profile.school = data["school"]
    
        db.session.commit()

        return profile


    @staticmethod
    def search_profiles(data):
        profiles = ProfileModel.query

        if data.get("age"):
            profiles = profiles.filter_by(age=data["age"])
        if data.get("location"):
            profiles = profiles.filter_by(location=data["location"])
        if data.get("sex"):
            profiles = profiles.filter_by(sex=data["sex"])
        if data.get("school"):
            profiles = profiles.filter_by(school=data["school"])

        profiles = profiles.all()

        if not profiles:
            raise NotFound("No profiles found")

        return profiles
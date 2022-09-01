from flask_restful import Resource, reqparse
from flask import request, jsonify
import json
from models.profile import ProfileModel

from managers.profile import ProfileManager
from managers.auth import AuthManager, auth


class ProfileResource(Resource):

    @auth.login_required
    def post(self):
        data = request.get_json()
        user_id = data["user_id"]
        profile = ProfileManager.create_profile(data)

        return {"message": "Profile successfully created"}, 201


class ProfileSearchResource(Resource):

    @auth.login_required
    def get(self):
        parser = reqparse.RequestParser() #bundle_errors=True
        parser.add_argument("age", type=int, required=False)
        parser.add_argument("location", type=str, required=False)
        parser.add_argument("sex", type=str, required=False)
        parser.add_argument("school", type=str, required=False)
        data = parser.parse_args()
        profiles = ProfileManager.search_profiles(data)
        
        return {"profiles": [profile.serialize() for profile in profiles]}, 200
from decouple import config
from flask_restful import Resource
from flask import request
from werkzeug.security import generate_password_hash

from db import db
from managers.auth import AuthManager

from managers.user import UserManager
from models.user import UserModel

from schemas.auth import RegisterRequestSchema, LoginRequestSchema

from utils.decorators import validate_schema


class RegisterResource(Resource):
    @validate_schema(RegisterRequestSchema)
    def post(self):
        data = request.get_json()
        token = UserManager.register(data)

        return {"token":  token}, 201
        
class LoginResource(Resource):
    @validate_schema(LoginRequestSchema)
    def post(self):
        data = request.get_json()
        token = UserManager.login(data)
        
        return {"token:": token}, 200
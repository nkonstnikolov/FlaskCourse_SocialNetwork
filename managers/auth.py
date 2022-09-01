from datetime import datetime, timedelta
import jwt
from decouple import config
from flask_httpauth import HTTPTokenAuth
from jwt import ExpiredSignatureError, InvalidTokenError
from werkzeug.exceptions import BadRequest, Unauthorized

from models.user import UserModel

auth = HTTPTokenAuth()

class AuthManager:

    @staticmethod
    def encode_token(user):
            payload = {
                "exp": datetime.utcnow() + timedelta(days=1),
                "sub": (user.user_id)
            }
            return jwt.encode(payload, key=config("SECRET_KEY"), algorithm="HS256")
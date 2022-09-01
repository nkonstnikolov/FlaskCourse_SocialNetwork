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
        payload = {'exp': datetime.utcnow() + timedelta(days=1),
                   'sub': user.user_id}
        return jwt.encode(payload, key=config('SECRET_KEY'),
                          algorithm='HS256')

    @staticmethod
    def decode_token(token):
        if not token:
            raise Unauthorized('You need a token for access to this resource'
                               )
        try:
            payload = jwt.decode(token, key=config('SECRET_KEY',
                                 algorithm='HS256'))
            return payload['sub']
        except ExpiredSignatureError:
            raise Unauthorized('Your token has expired. Please log in again.'
                               )
        except InvalidTokenError:
            raise Unauthorized('Invalid token')


@auth.verify_token
def verify(token):
    user_id = AuthManager.decode_token(token)

    return UserModel.query.filter_by(user_id=user_id).first()
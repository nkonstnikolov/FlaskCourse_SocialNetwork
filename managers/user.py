from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash
from db import db
from managers.auth import AuthManager
from models.user import UserModel
from models.enums import UserRole

class UserManager:

    @staticmethod
    def register(user_data):
    
        user_data['password'] = generate_password_hash(user_data['password'])
        user = UserModel(**user_data)
        db.session.add(user)
        db.session.commit()
        
        return AuthManager.encode_token(user)
from marshmallow import fields, validate

from schemas.base import BaseRegisterRequestSchema, BaseLogInRequestSchema


class RegisterRequestSchema(BaseRegisterRequestSchema):
    first_name = fields.String(required=True, validate=validate.Length(min=2, max=20))
    last_name = fields.String(required=True, validate=validate.Length(min=2, max=20))
    username = fields.String(required=True)
    user_role = fields.String(required=True)
    
class LoginRequestSchema(BaseLogInRequestSchema):
    username = fields.String(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6, max=255))
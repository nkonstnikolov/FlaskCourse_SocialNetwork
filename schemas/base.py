from decouple import config
from marshmallow import Schema, fields, validate

from utils.general_validators import validate_password


class AuthBase(Schema):

    email = fields.Email(required=True)
    password = fields.Str(
        required=True,
        validate=validate.And(
            validate.Length(
                min=6,
                max=255,
            ),
            validate_password,
        ),
    )
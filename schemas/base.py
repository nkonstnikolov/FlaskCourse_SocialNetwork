from marshmallow import Schema, fields, validate, validates, ValidationError
from password_policy import policy


class BaseRegisterRequestSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6, max=255))

    @validates("password")
    def validate_password(self, value):
        errors = policy.test(value)
        if errors:
            raise ValidationError(
                f"The password does not meet the requirements: {errors}"
            )


class BaseLogInRequestSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6, max=255))
from decouple import config
from flask import request
from werkzeug.exceptions import BadRequest


def validate_password(password):
    """
    Validates that the password meets the requirements for min/max length, types of symbols (lowercase and uppercase
    letter), at least one digit, at least one special symbol (it also defines special symbols).
    :param password: string; password, provided by the user
    :return Nothing, if the password is valid; BadRequest, if the password is invalid
    """
    special_symbols = [
        "$",
        "@",
        "#",
        "%",
        "^",
        "*",
        ")",
        ".",
        "(",
        "-",
        "=",
        "!",
        "&",
        "+",
    ]
    if len(password) < 6):
        raise BadRequest(
            f"Your password is too short, it needs to have at least 6 characters."
        )

    if len(password) > 255):
        raise BadRequest(
            f"Your password is too long, it needs to have at most 255 characters."
        )

    if not any(char.isdigit() for char in password):
        raise BadRequest("Your password should have at least one digit.")

    if not any(char.isupper() for char in password):
        raise BadRequest("Your password should have at least one uppercase letter")

    if not any(char.islower() for char in password):
        raise BadRequest("Your password should have at least one lowercase letter")

    if not any(char in special_symbols for char in password):
        raise BadRequest(
            f"Password should have at least one of the special symbols {special_symbols}"
        )
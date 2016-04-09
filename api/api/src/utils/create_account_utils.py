from api.src.constants.enums.error_enums import BadAuthEnum
from api.src.constants.exceptions.handler_exceptions import BadAuthException
from django.db import IntegrityError
from passlib.hash import bcrypt
from api.src.models.user_model import UserModel


def create_user(first_name, last_name, email, password):
    user = UserModel(first_name=first_name, last_name=last_name, email=email)
    try:
        user.save()
    except IntegrityError as e:
        raise BadAuthException(BadAuthEnum.AUTH_EXISTS)

    # password hashing is slow, so we should do this only if necessary
    user.password_hash = hash_password(password)
    user.save()

    return user


def hash_password(password):
    # print 'sign up hashed pw', bcrypt.encrypt(password, rounds=12)
    return bcrypt.encrypt(password, rounds=4)


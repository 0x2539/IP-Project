import jwt
from api.src.constants.enums.error_enums import BadAuthEnum
from api.src.constants.exceptions.handler_exceptions import BadAuthException
from api.src.models.user_model import UserModel
from django.core.exceptions import ObjectDoesNotExist
from passlib.hash import bcrypt
from api import settings
from api.src.utils.utils import get_now


def create_login_data(user):

    token = generate_login_token(user)
    login_data = {
        'token': token,
        'fb_user_id': user.fb_user_id,
    }
    return login_data


def get_token_data(authorization_header):

    if authorization_header is None:
        return {
            'success': False,
            'error': 'NO_AUTHORIZATION_HEADER'
        }

    try:
        token = authorization_header.split()[1]
        decoded = jwt.decode(token, settings.JWT_API_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError as e:
        return {
            'success': False,
            'error': 'EXPIRED_TOKEN'
        }
    except Exception as e:
        return {
            'success': False,
            'error': 'LOGIN_INVALID'
        }
    return {
        'success': True,
        'token_data': decoded,
    }


def generate_login_token(user):
    """
        Generates a JWT token containing provider information.
    :param user_id:
    :return:
    """
    expiry = get_now() + settings.JWT_EXPIRY_DAYS * 1000 * 60 * 60 * 24
    payload = {
        'id': user.id,
        'user_type': user.user_type,
        'exp': expiry,
    }
    encoded = jwt.encode(payload, settings.JWT_API_KEY, algorithm='HS256')
    return encoded


def login(email, password):

    if password == '' or password is None:
        raise BadAuthException(BadAuthEnum.EMPTY_PASSWORD)

    try:
        user = UserModel.objects.get(email=email)
    except ObjectDoesNotExist:
        raise BadAuthException(BadAuthEnum.WRONG_AUTH)

    if not __check_password(password, user.password_hash):
        raise BadAuthException(BadAuthEnum.WRONG_PASSWORD)

    return create_login_data(user)


def __check_password(password, password_db):

    # return True
    if password is None or len(password) == 0:
        return False

    return bcrypt.verify(password, password_db)

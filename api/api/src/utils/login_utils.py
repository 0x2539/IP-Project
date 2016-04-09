import jwt
from api import settings


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


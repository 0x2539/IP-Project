import httplib
import json
import logging
import urllib2

from api import settings
from api.src.constants.enums.error_enums import BadAuthEnum
from api.src.constants.exceptions.handler_exceptions import BadAuthException
from api.src.models.user_model import UserModel
from django.core.exceptions import ObjectDoesNotExist

FACEBOOK_PROVIDER = "facebook"


# Makes a Facebook Graph API request to retrieve profile information.
def fb_get_user_info(user_id, auth_token):
    user_info = {}
    status = {
        "message": "",
        "code": httplib.OK
    }
    get_profile_info_url = "https://graph.facebook.com/" + user_id + \
                           "?fields=email,id,name,picture" + \
                           "&access_token=" + auth_token
    try:
        response = urllib2.urlopen(get_profile_info_url)

        profile = response.read()
        profile_data = json.loads(profile)

        user_info = {
            "email": profile_data['email'],
            "name": profile_data['name'],
            "avatar_url": profile_data['picture']['data']['url']
        }
    except:
        status['message'] = "Error getting profile info"
        status['code'] = httplib.INTERNAL_SERVER_ERROR

    return user_info, status


# Check that the user granted the email permission for the Facebook app.
def fb_permission_check(token, user_id):
    user_perm_url = "https://graph.facebook.com/" + user_id + "/permissions?access_token=" + token

    try:
        response = urllib2.urlopen(user_perm_url)
    except:
        raise BadAuthException(BadAuthEnum.PERMISSION_DENIED)


# Verify the auth token for Facebook 3rd party login.
def fb_token_verification(token, user_id):

    # Auth Token verification
    token_verify_url = "https://graph.facebook.com/debug_token?" + \
                       "input_token=" + token + \
                       "&access_token=" + settings.FACEBOOK_APP_ID + "%7C" + settings.FACEBOOK_APP_SECRET
    logging.info(token_verify_url)

    logging.info("Facebook token verification: user_id=" + user_id + " token=" + token)

    try:
        response = urllib2.urlopen(token_verify_url)
    except:
        raise BadAuthException(BadAuthEnum.CANT_VERIFY_FACEBOOK_TOKEN)

    r = response.read()
    data = json.loads(r)

    if data['data']['is_valid'] is not True or data['data']['app_id'] != settings.FACEBOOK_APP_ID:
        raise BadAuthException(BadAuthEnum.INVALID_PROVIDER_TOKEN)


# The Facebook 3rd party login flow.
def fb_login(token, user_id):
    fb_token_verification(token, user_id)

    # Check granted permissions
    fb_permission_check(token, user_id)

    # Try fetching the user associated with the Facebook profile.
    try:
        user = UserModel.objects.get(UserModel.fb_user_id == user_id)
    except ObjectDoesNotExist as e:
        user = None

    if user is None:
        # There is no user associated with the facebook profile, create one.
        user = UserModel(fb_user_id=user_id)
        user.save()
    return user

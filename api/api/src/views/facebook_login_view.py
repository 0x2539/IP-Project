import httplib

from api.src.constants.exceptions.handler_exceptions import BadAuthException
from api.src.utils import schemas, facebook_login_utils, login_utils
from api.src.utils.decorators import validate_request
from api.src.views.base_view import BaseView


class FacebookLoginView(BaseView):

    @validate_request(schema=schemas.schema_facebook_login_post)
    def post(self, request, received_json):

        access_token = received_json.get('access_token')
        provider_user_id = received_json.get('provider_user_id')

        try:
            user = facebook_login_utils.fb_login(access_token, provider_user_id)
            login_data = login_utils.create_login_data(user)
        except BadAuthException as e:
            return self.send_failed(e.error.name)

        return self.send_success(login_data, httplib.OK)

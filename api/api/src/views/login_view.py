import httplib

from api.src.constants.exceptions.handler_exceptions import BadAuthException
from api.src.utils import schemas, login_utils
from api.src.utils.decorators import validate_request
from api.src.views.base_view import BaseView


class LoginView(BaseView):

    @validate_request(schema=schemas.schema_login_post)
    def post(self, request, received_json):

        email = received_json.get('email')
        password = received_json.get('password')

        try:
            login_data = login_utils.login(email, password)
        except BadAuthException as e:
            return self.send_failed(e.error.name)

        return self.send_success(login_data, httplib.OK)

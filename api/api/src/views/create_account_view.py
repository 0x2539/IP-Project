import httplib

from api.src.constants.exceptions.handler_exceptions import BadAuthException
from api.src.utils import schemas, create_account_utils, login_utils
from api.src.utils.decorators import validate_request
from api.src.views.base_view import BaseView


class CreateAccountView(BaseView):

    @validate_request(schema=schemas.schema_create_account_put)
    def put(self, request, received_json):

        first_name = received_json.get('first_name')
        last_name = received_json.get('last_name')
        email = received_json.get('email')
        password = received_json.get('password')

        try:
            user = create_account_utils.create_user(first_name, last_name, email, password)
        except BadAuthException as e:
            return self.send_failed(e.error.name)

        return self.send_success(login_utils.create_login_data(user), httplib.OK)

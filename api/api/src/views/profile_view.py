import httplib

from api.src.constants.enums.user_type_enum import UserTypeEnum
from api.src.constants.exceptions.handler_exceptions import BadAuthException
from api.src.models.user_model import UserModel, UserSerializer
from api.src.utils import schemas, create_account_utils, login_utils
from api.src.utils.decorators import validate_request
from api.src.views.base_view import BaseView


class ProfileView(BaseView):

    @validate_request(user_required=UserTypeEnum.NORMAL)
    def get(self, request, user_id, token_payload):
        return self.get_one_or_all(request, UserModel, UserSerializer, user_id)

    @validate_request(schema=schemas.schema_profile_post, user_required=UserTypeEnum.NORMAL)
    def post(self, request, received_json, user_id, token_payload):
        received_json['id'] = user_id
        return self.post_one(request, received_json, UserModel)

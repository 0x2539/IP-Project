from api.src.constants.enums.user_type_enum import UserTypeEnum
from api.src.models.category_model import CategoryModel, CategorySerializer
from api.src.utils import schemas
from api.src.utils.decorators import validate_request
from api.src.views.base_view import BaseView


class CategoryView(BaseView):

    @validate_request()
    def get(self, request, category_id=None):
        return self.get_one_or_all(request, CategoryModel, CategorySerializer,  category_id)

    @validate_request(schema=schemas.schema_category_post, user_required=UserTypeEnum.NORMAL)
    def post(self, request, received_json, user_id, token_payload):
        return self.post_one(request, received_json, CategoryModel)

    @validate_request(schema=schemas.schema_category_put, user_required=UserTypeEnum.NORMAL)
    def put(self, request, received_json, user_id, token_payload):
        return self.put_one(request, received_json, CategoryModel)

    @validate_request(schema=schemas.schema_category_delete, user_required=UserTypeEnum.NORMAL)
    def delete(self, request, received_json, user_id, token_payload, category_id):
        return self.delete_one(request, received_json, CategoryModel, category_id)

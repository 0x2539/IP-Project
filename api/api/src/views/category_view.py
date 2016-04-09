from api.src.models.category_model import CategoryModel, CategorySerializer
from api.src.utils import schemas
from api.src.utils.decorators import validate_request
from api.src.views.base_view import BaseView


class CategoryView(BaseView):

    @validate_request()
    def get(self, request, category_id=None):
        return self.get_one_or_all(request, CategoryModel, CategorySerializer,  category_id)

    @validate_request(schema=schemas.schema_category_post)
    def post(self, request, received_json, category_id=None):
        return self.post_one(request, received_json, CategoryModel)

    @validate_request(schema=schemas.schema_category_put)
    def put(self, request, received_json, category_id=None):
        return self.put_one(request, received_json, CategoryModel)

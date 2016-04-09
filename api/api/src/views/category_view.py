import httplib

from api.src.models.category_model import CategoryModel, CategorySerializer
from api.src.utils import schemas
from api.src.utils.decorators import validate_request
from api.src.views.base_view import BaseView
from django.core.exceptions import ObjectDoesNotExist


class CategoryView(BaseView):

    @validate_request()
    def get(self, request, category_id=None):
        return self.get_one_or_all(request, CategoryModel, CategorySerializer,  category_id)

    @validate_request(schema=schemas.schema_tip_and_trick_post)
    def post(self, request, received_json, tip_and_trick_id=None):

        tip_and_trick_id = received_json.get('id')
        title = received_json.get('title')
        description = received_json.get('description')

        try:
            tip_and_trick = TipAndTrickModel.objects.get(pk=tip_and_trick_id)
        except ObjectDoesNotExist as e:
            return self.send_failed('tip and trick not found', httplib.BAD_REQUEST)

        tip_and_trick.title = title
        tip_and_trick.description = description
        tip_and_trick.save()

        return self.send_success({}, httplib.OK)

    @validate_request(schema=schemas.schema_tip_and_trick_put)
    def put(self, request, received_json, tip_and_trick_id=None):

        title = received_json.get('title')
        description = received_json.get('description')

        tip_and_trick = TipAndTrickModel(title=title, description=description)
        tip_and_trick.save()

        return self.send_success({'tip_and_trick_id': tip_and_trick.id}, httplib.OK)

from api.src.models.rating_model import RatingModel, RatingSerializer
from api.src.utils import schemas
from api.src.utils.decorators import validate_request
from api.src.views.base_view import BaseView


class RatingApplyView(BaseView):

    @validate_request()
    def get(self, request, rating_id=None):
        return self.get_one_or_all(request, RatingModel, RatingSerializer, rating_id)

    @validate_request(schema=schemas.schema_tip_and_trick_rating_post)
    def post(self, request, received_json, rating_id=None):
        received_json['user_id'] = 1
        return self.post_one(request, received_json, RatingModel)

    @validate_request(schema=schemas.schema_tip_and_trick_rating_put)
    def put(self, request, received_json, rating_id=None):
        received_json['user_id'] = 1
        return self.put_one(request, received_json, RatingModel)
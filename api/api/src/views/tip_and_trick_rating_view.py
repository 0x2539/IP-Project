from api.src.models.tip_and_trick_model import TipAndTrickModel, TipAndTrickSerializer
from api.src.utils import schemas
from api.src.utils.decorators import validate_request
from api.src.views.base_view import BaseView


class TipAndTrickRatingView(BaseView):

    @validate_request()
    def get(self, request, tip_and_trick_id, rating_id=None):
        return self.get_one_or_all(request, TipAndTrickModel, TipAndTrickSerializer,  tip_and_trick_id)

    @validate_request(schema=schemas.schema_tip_and_trick_post)
    def post(self, request, received_json, tip_and_trick_id, rating_id=None):
        return self.post_one(request, received_json, TipAndTrickModel)

    @validate_request(schema=schemas.schema_tip_and_trick_put)
    def put(self, request, received_json, tip_and_trick_id, rating_id=None):
        return self.put_one(request, received_json, TipAndTrickModel)

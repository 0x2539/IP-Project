import httplib

from api.src.constants.enums.user_type_enum import UserTypeEnum
from api.src.models.rating_model import RatingModel, RatingSerializer
from api.src.models.tip_and_trick_model import TipAndTrickModel
from api.src.utils import schemas
from api.src.utils.decorators import validate_request
from api.src.views.base_view import BaseView
from django.core.exceptions import ObjectDoesNotExist


class RatingApplyView(BaseView):

    @validate_request()
    def get(self, request, rating_id=None):
        return self.get_one_or_all(request, RatingModel, RatingSerializer, rating_id)

    @validate_request(schema=schemas.schema_tip_and_trick_rating_post, user_required=UserTypeEnum.NORMAL)
    def post(self, request, received_json, user_id, token_payload):
        received_json['user_id'] = user_id
        return self.post_one(request, received_json, RatingModel)

    @validate_request(schema=schemas.schema_tip_and_trick_rating_put, user_required=UserTypeEnum.NORMAL)
    def put(self, request, received_json, user_id, token_payload):
        try:
            received_json['user_id'] = user_id

            tip_and_trick = TipAndTrickModel.objects.get(pk=received_json['tip_and_trick_id'])

            number_of_ratings = tip_and_trick.number_of_ratings

            tip_and_trick.number_of_ratings = number_of_ratings + 1
            tip_and_trick.average_rating = (tip_and_trick.average_rating * number_of_ratings + received_json['rating']) / (number_of_ratings + 1)

            tip_and_trick.save()

        except ObjectDoesNotExist as e:
            return self.send_failed('item not found', httplib.BAD_REQUEST)
        return self.put_one(request, received_json, RatingModel)

    @validate_request(schema=schemas.schema_tip_and_trick_rating_delete, user_required=UserTypeEnum.NORMAL)
    def delete(self, request, received_json, user_id, token_payload, rating_id):
        return self.delete_one(request, received_json, RatingModel, rating_id)

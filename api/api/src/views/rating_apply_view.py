import httplib

from api.src.constants.enums.user_type_enum import UserTypeEnum
from api.src.models.rating_model import RatingModel, RatingSerializer
from api.src.models.tip_and_trick_model import TipAndTrickModel
from api.src.utils import schemas, rating_apply_utils
from api.src.utils.decorators import validate_request
from api.src.views.base_view import BaseView
from django.core.exceptions import ObjectDoesNotExist


class RatingApplyView(BaseView):

    @validate_request()
    def get(self, request, rating_id=None):
        return self.get_one_or_all(request, RatingModel, RatingSerializer, rating_id)

    @validate_request(schema=schemas.schema_tip_and_trick_rating_post, user_required=UserTypeEnum.NORMAL)
    def post(self, request, received_json, user_id, token_payload):
        try:
            received_json['user_id'] = user_id

            tip_and_trick = TipAndTrickModel.objects.get(pk=received_json['tip_and_trick_id'])
            rating = RatingModel.objects.get(pk=received_json['id'])

            tip_and_trick = rating_apply_utils.update_rating(tip_and_trick, received_json['rating'], rating.rating)

            tip_and_trick.save()

        except ObjectDoesNotExist as e:
            return self.send_failed('item not found', httplib.BAD_REQUEST)
        return self.post_one(request, received_json, RatingModel)

    @validate_request(schema=schemas.schema_tip_and_trick_rating_put, user_required=UserTypeEnum.NORMAL)
    def put(self, request, received_json, user_id, token_payload):
        try:
            received_json['user_id'] = user_id

            tip_and_trick = TipAndTrickModel.objects.get(pk=received_json['tip_and_trick_id'])

            tip_and_trick = rating_apply_utils.add_rating(tip_and_trick, received_json['rating'])

            tip_and_trick.save()

        except ObjectDoesNotExist as e:
            return self.send_failed('item not found', httplib.BAD_REQUEST)
        return self.put_one(request, received_json, RatingModel)

    @validate_request(schema=schemas.schema_tip_and_trick_rating_delete, user_required=UserTypeEnum.NORMAL)
    def delete(self, request, received_json, user_id, token_payload, rating_id):
        return self.delete_one(request, received_json, RatingModel, rating_id)

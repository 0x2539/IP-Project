from api.src.models.rating_model import RatingModel, RatingSerializer
from api.src.utils import schemas
from api.src.utils.decorators import validate_request
from api.src.views.base_view import BaseView


class RatingTipAndTrickView(BaseView):

    @validate_request()
    def get(self, request, tip_and_trick_id=None):

        is_this_tip_and_trick_filter = {}
        if tip_and_trick_id is not None:
            is_this_tip_and_trick_filter = {'tip_and_trick': tip_and_trick_id}
            # return self.send_failed('MISSING_TIP_AND_TRICK_ID')

        return self.get_one_or_all(
            request,
            RatingModel,
            RatingSerializer,
            filters=is_this_tip_and_trick_filter
        )

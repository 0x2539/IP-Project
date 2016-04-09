from api.src.models.base_model import BaseModel
from api.src.models.tip_and_trick_model import TipAndTrickModel
from api.src.models.user_model import UserModel
from rest_framework import serializers
from django.db import models


class RatingModel(BaseModel):
    rating = models.PositiveSmallIntegerField()
    tip_and_trick = models.ForeignKey(TipAndTrickModel)
    user = models.ForeignKey(UserModel)


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = RatingModel
        fields = ('id', 'rating', 'date_modified', 'tip_and_trick', 'user')

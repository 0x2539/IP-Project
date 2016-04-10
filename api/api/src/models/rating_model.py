from api.src.models.base_model import BaseModel
from api.src.models.tip_and_trick_model import TipAndTrickModel
from api.src.models.user_model import UserModel
from rest_framework import serializers
from django.db import models


class RatingModel(BaseModel):
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    tip_and_trick = models.ForeignKey(TipAndTrickModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('tip_and_trick', 'user',)


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = RatingModel
        fields = ('id', 'rating', 'comment', 'tip_and_trick', 'user', 'date_modified')

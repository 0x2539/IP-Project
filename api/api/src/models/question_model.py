from api.src.models.base_model import BaseModel
from rest_framework import serializers
from django.db import models


class QuestionModel(BaseModel):
    title = models.CharField(max_length=255)
    message = models.TextField()


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionModel
        fields = ('title', 'message', 'date_created', 'date_modified')

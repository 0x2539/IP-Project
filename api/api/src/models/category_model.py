from api.src.models.base_model import BaseModel
from rest_framework import serializers
from django.db import models


class CategoryModel(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = ('id', 'title', 'description', 'date_created', 'date_modified')

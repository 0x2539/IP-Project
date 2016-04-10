from api.src.constants.enums.user_type_enum import UserTypeEnum
from api.src.models.base_model import BaseModel
from rest_framework import serializers
from django.db import models


class UserModel(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=255)
    fb_user_id = models.CharField(max_length=255)
    user_type = models.IntegerField(default=UserTypeEnum.NORMAL.value)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ('id', 'first_name', 'last_name', 'email', 'fb_user_id', 'user_type')

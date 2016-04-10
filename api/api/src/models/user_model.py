from api.src.constants.enums.user_type_enum import UserTypeEnum
from api.src.models.base_model import BaseModel
from rest_framework import serializers
from django.db import models


class UserModel(BaseModel):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, unique=True, null=True, blank=True)
    password_hash = models.CharField(max_length=255, null=True, blank=True)
    fb_user_id = models.CharField(max_length=255, null=True, blank=True)
    user_type = models.IntegerField(default=UserTypeEnum.NORMAL.value)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ('id', 'first_name', 'last_name', 'email', 'fb_user_id', 'user_type')

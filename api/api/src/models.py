from api.src.utils.utils import get_now
from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    date_created = models.BigIntegerField(default=get_now)
    date_modified = models.BigIntegerField(default=get_now)

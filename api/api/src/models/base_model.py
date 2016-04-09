from api.src.utils.utils import get_now
from django.db import models


class BaseModel(models.Model):
    date_created = models.BigIntegerField(default=get_now, editable=False)
    date_modified = models.BigIntegerField(default=get_now, editable=False)

    def save(self, **kwargs):
        # if not self.id:
        #     self.created = get_now()
        print 'saving'
        self.date_modified = get_now()
        super(BaseModel, self).save()

    class Meta:
        abstract = True  # Set this model as Abstract

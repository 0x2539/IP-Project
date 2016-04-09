from api.src.utils.utils import get_now
from django.db import models


class BaseModel(models.Model):
    date_created = models.BigIntegerField(default=get_now, editable=False)
    date_modified = models.BigIntegerField(editable=False)

    def save(self, **kwargs):
        self.date_modified = get_now()
        super(BaseModel, self).save()

    # def to_dict(self, body, skip=[], only=None, relationships=None):
    #     members = [attr for attr in vars(body) if not attr.startswith("__")]
    #
    #     columns = members
    #
    #     if only is not None:
    #         columns = [item for item in only if item in members]
    #
    #     if skip is not None:
    #         columns = [item for item in members if item not in skip]
    #
    #     result = {c: body.get(c) for c in columns}
    #
    #     return result

    class Meta:
        abstract = True  # Set this model as Abstract

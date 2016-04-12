import httplib

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.generic import View


class BaseView(View):

    def __send(self, body, http_code):
        return JsonResponse(body, status=http_code, safe=False)

    def send_success(self, body, http_code=httplib.OK):
        """

        :param body: should be a dict
        :param http_code: use httplib for codes
        :return:
        """
        return self.__send(body, http_code)

    def send_failed(self, error_message, http_code=httplib.BAD_REQUEST):
        """

        :param error_message: should be a string, like "PASSWORD_INCORRECT"
        :param http_code: use httplib for codes
        :return:
        """
        return self.__send({'error': error_message}, http_code)

    class Meta:
        abstract = True  # Set this class as Abstract

    def get_one_or_all(self, request, model, serializer, item_id=None, skip=[], only=[], filters={}):

        if item_id is None:
            if filters is not None:
                items = model.objects.filter(**filters)
            else:
                items = model.objects.all()
            items_dict = [serializer(item).data for item in items]
            # remove skipped columns
            if skip is not None and skip != []:
                for index, value in enumerate(items_dict):
                    for key in skip:
                        items_dict[index].pop(key, None)
            return self.send_success(items_dict)

        try:
            category = model.objects.get(pk=item_id)
        except ObjectDoesNotExist as e:
            return self.send_failed('item not found', httplib.BAD_REQUEST)

        data = serializer(category).data
        if skip is not None and skip != []:
            for key in skip:
                data.pop(key, None)
        return self.send_success(data, httplib.OK)

    def post_one(self, request, received_json, model, skip=[], only=[]):

        item_id = received_json.get('id')

        try:
            item = model.objects.get(pk=item_id)
        except ObjectDoesNotExist as e:
            return self.send_failed('item not found', httplib.BAD_REQUEST)

        values = {key: value for key, value in received_json.iteritems() if hasattr(item, key)}
        if skip is not None and skip != []:
            values = {key: value for key, value in received_json.iteritems() if key not in skip and hasattr(item, key)}
        elif only is not None and only != []:
            values = {key: value for key, value in received_json.iteritems() if key in only and hasattr(item, key)}

        for key, value in values.iteritems():
                setattr(item, key, value)

        item.save()

        return self.send_success({}, httplib.OK)

    def put_one(self, request, received_json, model, skip=[], only=[]):

        attrs = vars(model())
        values = {key: value for key, value in received_json.iteritems() if key in attrs}
        if skip is not None and skip != []:
            values = {key: value for key, value in received_json.iteritems() if key not in skip and key in attrs}
        elif only is not None and only != []:
            values = {key: value for key, value in received_json.iteritems() if key in only and key in attrs}

        try:
            item = model(**values)
            item.save()
        except IntegrityError as e:
            return self.send_failed('item already exists', httplib.BAD_REQUEST)

        return self.send_success({}, httplib.OK)

    def delete_one(self, request, received_json, model, item_id):

        try:
            item = model.objects.get(pk=item_id)
        except ObjectDoesNotExist as e:
            return self.send_failed('item not found', httplib.BAD_REQUEST)

        item.delete()

        return self.send_success({}, httplib.OK)

import httplib
import json

from api.src.models.question_model import QuestionModel, QuestionSerializer
from django.http import JsonResponse
from django.views.generic import View

from api.src.utils.utils import is_string_empty, get_now


class BaseView(View):

    def __send(self, body, http_code):
        return JsonResponse(body, status=http_code)

    def send_success(self, body, http_code=httplib.OK):
        return JsonResponse(body, status=http_code)

    def send_failed(self, error_message, http_code=httplib.BAD_REQUEST):
        return JsonResponse({'error': error_message}, status=http_code)

    class Meta:
        abstract = True  # Set this class as Abstract

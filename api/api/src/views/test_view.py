import httplib
import json

from api.src.models.question_model import QuestionModel, QuestionSerializer
from django.http import JsonResponse
from django.views.generic import View

from api.src.utils.utils import is_string_empty, get_now


class TestView(View):

    def get(self, request, question_id=None):

        # id = request.GET.get('id', 3)

        question = QuestionModel.objects.get(pk=question_id)
        serializer = QuestionSerializer(question)
        response = {
            'some': 'value',
            'data': serializer.data,
            'time': get_now(),
            'url_value': question_id,
            'what': 'this is test',
        }
        return JsonResponse(response, status=httplib.OK)

    def post(self, request):
        received_json = json.loads(request.body)

        title = received_json.get('title')
        message = received_json.get('message')

        if is_string_empty(title) or is_string_empty(message):
            return JsonResponse({'error': 'json is incomplete'}, status=httplib.BAD_REQUEST)

        question = QuestionModel(title=title, message=message)
        question.save()

        response = {
            'saved': question.id
        }
        return JsonResponse(response, status=httplib.OK)

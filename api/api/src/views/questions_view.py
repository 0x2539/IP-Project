import httplib
import json

from api.src.models import Question
from api.src.serializers import QuestionSerializer
from django.http import JsonResponse
from django.views.generic import View

from api.src.utils.utils import is_string_empty, get_now


class QuestionsView(View):

    def get(self, request):

        id = request.GET.get('id', 3)

        question = Question.objects.get(pk=id)
        serializer = QuestionSerializer(question)
        response = {
            'some': 'value',
            'data': serializer.data,
            'time': get_now(),
        }
        return JsonResponse(response, status=httplib.OK)

    def post(self, request):
        received_json = json.loads(request.body)

        title = received_json.get('title')
        message = received_json.get('message')

        if is_string_empty(title) or is_string_empty(message):
            return JsonResponse({'error': 'json is incomplete'}, status=httplib.BAD_REQUEST)

        question = Question(title=title, message=message)
        question.save()

        response = {
            'saved': question.id
        }
        return JsonResponse(response, status=httplib.OK)

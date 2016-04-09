import httplib
import json

from api.src.models.question_model import QuestionModel, QuestionSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.generic import View

from api.src.utils.utils import is_any_string_empty, get_now


class QuestionsView(View):

    def get(self, request):

        question_id = request.GET.get('id', 3)

        try:
            question = QuestionModel.objects.get(pk=question_id)
        except ObjectDoesNotExist as e:
            return JsonResponse({'error': 'question not found'}, status=httplib.BAD_REQUEST)

        serializer = QuestionSerializer(question)
        response = {
            'some': 'value',
            'data': serializer.data,
            'time': get_now(),
        }
        return JsonResponse(response, status=httplib.OK)

    def post(self, request):
        received_json = json.loads(request.body)

        question_id = received_json.get('id')
        title = received_json.get('title')
        message = received_json.get('message')

        if is_any_string_empty([question_id, title, message]):
            return JsonResponse({'error': 'json is incomplete'}, status=httplib.BAD_REQUEST)

        try:
            question = QuestionModel.objects.get(pk=question_id)
        except ObjectDoesNotExist as e:
            return JsonResponse({'error': 'question not found'}, status=httplib.BAD_REQUEST)

        question.title = title
        question.message = message
        question.save()

        response = {
            'saved': question.id
        }
        return JsonResponse(response, status=httplib.OK)

    def put(self, request):
        received_json = json.loads(request.body)

        title = received_json.get('title')
        message = received_json.get('message')

        if is_any_string_empty([title, message]):
            return JsonResponse({'error': 'json is incomplete'}, status=httplib.BAD_REQUEST)

        question = QuestionModel(title=title, message=message)
        question.save()

        response = {
            'saved': question.id
        }
        return JsonResponse(response, status=httplib.OK)

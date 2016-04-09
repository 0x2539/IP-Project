import httplib
import json

from api.src.models.question_model import QuestionModel, QuestionSerializer
from api.src.utils import schemas
from api.src.utils.decorators import validate_request
from api.src.views.base_view import BaseView
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from api.src.utils.utils import is_any_string_empty, get_now


class QuestionsView(BaseView):

    @validate_request()
    def get(self, request):

        question_id = request.GET.get('id', 3)

        try:
            question = QuestionModel.objects.get(pk=question_id)
        except ObjectDoesNotExist as e:
            return self.send_failed('question not found', httplib.BAD_REQUEST)

        serializer = QuestionSerializer(question)
        response = {
            'some': 'value',
            'data': serializer.data,
            'time': get_now(),
        }
        return self.send_success(response, httplib.OK)

    @validate_request(schema=schemas.schema_question_post)
    def post(self, request, received_json):

        question_id = received_json.get('id')
        title = received_json.get('title')
        message = received_json.get('message')

        try:
            question = QuestionModel.objects.get(pk=question_id)
        except ObjectDoesNotExist as e:
            return self.send_failed('question not found', httplib.BAD_REQUEST)

        question.title = title
        question.message = message
        question.save()

        response = {
            'saved': question.id
        }
        return self.send_success(response, httplib.OK)

    @validate_request(schema=schemas.schema_question_put)
    def put(self, request, received_json):

        title = received_json.get('title')
        message = received_json.get('message')

        question = QuestionModel(title=title, message=message)
        question.save()

        response = {
            'saved': question.id
        }
        return self.send_success(response, httplib.OK)

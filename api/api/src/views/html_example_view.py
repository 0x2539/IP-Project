from api.src.constants.enums.user_type_enum import UserTypeEnum
from api.src.models.user_model import UserModel
from api.src.utils import schemas, create_account_utils
from api.src.utils.decorators import validate_request
from api.src.views.base_view import BaseView
from django.shortcuts import render_to_response


class HtmlExampleView(BaseView):
    # @validate_request(user_required=UserTypeEnum.ADMIN)

    def get(self, request):
        # def get(self, request, user_id, token_payload, item_id=None):
        # template = loader.get_template('html_example.html')
        # context = Context({ 'object_list': UserModel.objects.all() })
        # return template.render(context)
        if request.session.get("fav_color") is None:
            print 'session color is none'
            request.session["fav_color"] = "blue"
        else:
            print 'the color is:', request.session["fav_color"]

        return render_to_response('html_example.html', {'object_list': UserModel.objects.all()})

    @validate_request(schema=schemas.schema_users_post, user_required=UserTypeEnum.ADMIN)
    def post(self, request, received_json, user_id, token_payload):
        received_json['password_hash'] = create_account_utils.hash_password(received_json['password'])
        return self.post_one(request, received_json, UserModel)

    @validate_request(schema=schemas.schema_users_put, user_required=UserTypeEnum.ADMIN)
    def put(self, request, received_json, user_id, token_payload):
        received_json['password_hash'] = create_account_utils.hash_password(received_json['password'])
        return self.put_one(request, received_json, UserModel)

    @validate_request(schema=schemas.schema_users_delete, user_required=UserTypeEnum.ADMIN)
    def delete(self, request, received_json, user_id, token_payload, item_id):
        return self.delete_one(request, received_json, UserModel, item_id)

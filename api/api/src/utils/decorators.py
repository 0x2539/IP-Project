import httplib
import json

import jsonschema
from api.src.utils import login_utils


def validate_request(schema=None, schema_attribute=None, user_required=None):
    """
      Decorator needed for parameter.
    """

    def validate_request_decorator(handler):
        """
          Decorator that checks if the given json is valid and returns the object corresponding to that json.
          Will fail if the json format is invalid.
          Will fail if the json schema is wrong.
        """

        def check_request(self, *args, **kwargs):
            # request = kwargs.get('request', None)
            request = args[0]
            if request is None:
                return self.send_failed('request is missing')

            # validating json
            schema_name = getattr(self, schema_attribute) if schema_attribute is not None else schema
            if schema_name is not None:
                json_body, code = check_json(schema_name, request)
                if code is not httplib.OK:
                    return self.send_failed(json_body, code)

                kwargs['received_json'] = json_body

            # logging in user
            if user_required is not None:

                authorization_header = request.META.get('HTTP_AUTHORIZATION')
                if authorization_header is None:
                    return self.send_failed('AUTHORIZATION_HEADER_MISSING', httplib.UNAUTHORIZED)

                try:
                    token_payload = check_user_required(authorization_header, user_required)
                except Exception as e:
                    return self.send_failed(e.message, httplib.UNAUTHORIZED)

                kwargs['token_payload'] = token_payload
                kwargs['user_id'] = int(token_payload['id'])

            return handler(self, *args, **kwargs)

        return check_request

    return validate_request_decorator


def check_json(schema, request):
    try:
        body = json.loads(request.body)
    except ValueError as e:
        error_message = "JSON validation failed. JSON can't be loaded, error: %s" % e.message
        http_code = httplib.BAD_REQUEST
        return error_message, http_code

    try:
        jsonschema.validate(body, schema)
        return body, httplib.OK

    except jsonschema.exceptions.ValidationError as e:
        error_message = "JSON validation failed. JSON doesn't follow the schema. " \
                        "Error message validation: {:s}".format(e.message)
        http_code = httplib.BAD_REQUEST
        return error_message, http_code

    except jsonschema.exceptions.SchemaError as e:
        error_message = "JSON validation failed. JSON doesn't follow the schema. " \
                        "Error message schema: {:s}".format(e.message)
        http_code = httplib.BAD_REQUEST
        return error_message, http_code


def check_user_required(authorization_header, user_required):
    token_data_response = login_utils.get_token_data(authorization_header)

    if not token_data_response.get('success'):
        raise Exception('TOKEN_IS_INVALID')

    token_payload = token_data_response.get('token_data')

    # user_type = token_payload.get('user_type')
    # if user_type < user_required.value:
    #     raise Exception('NOT_ENOUGH_PERMISSIONS %s:%s' % (user_type, user_required.value))

    return token_payload


def check_json_has_paramters(json, parameters):
    for parameter in parameters:
        if json.get(parameter) is None:
            return False
    return True

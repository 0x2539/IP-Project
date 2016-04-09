
schema_question_post = {
    'type': 'object',
    'required': ['id', 'title', 'message'],
    'additionalProperties': False,
    'properties': {
        'id': {'type': 'integer'},
        'title': {'type': 'string'},
        'message': {'type': 'string'},
    },
}

schema_question_put = {
    'type': 'object',
    'required': ['id', 'title', 'message'],
    'additionalProperties': False,
    'properties': {
        'id': {'type': 'integer'},
        'title': {'type': 'string'},
        'message': {'type': 'string'},
    },
}

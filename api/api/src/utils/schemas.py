
schema_create_account_put = {
    'type': 'object',
    'required': ['first_name', 'last_name'],
    'additionalProperties': False,
    'properties': {
        'first_name': {'type': 'string'},
        'last_name': {'type': 'string'},
        'email': {
            'type': 'string',
            'pattern': '[^@]+@[^@]+\.[^@]+'
        },
        'password': {'type': 'string'},
    },
}

schema_login_post = {
    'type': 'object',
    'required': ['email', 'password'],
    'additionalProperties': False,
    'properties': {
        'email': {
            'type': 'string',
            'pattern': '[^@]+@[^@]+\.[^@]+'
        },
        'password': {'type': 'string'},
    },
}

schema_profile_post = {
    'type': 'object',
    'additionalProperties': False,
    'properties': {
        'first_name': {'type': 'string'},
        'last_name': {'type': 'string'},
        'email': {
            'type': 'string',
            'pattern': '[^@]+@[^@]+\.[^@]+'
        },
    },
}

schema_tip_and_trick_post = {
    'type': 'object',
    'required': ['id', 'title', 'description', 'category_id'],
    'additionalProperties': False,
    'properties': {
        'id': {'type': 'integer'},
        'title': {'type': 'string'},
        'description': {'type': 'string'},
        'category_id': {'type': 'integer'},
    },
}

schema_tip_and_trick_put = {
    'type': 'object',
    'required': ['title', 'description', 'category_id'],
    'additionalProperties': False,
    'properties': {
        'title': {'type': 'string'},
        'description': {'type': 'string'},
        'category_id': {'type': 'integer'},
    },
}


schema_tip_and_trick_rating_post = {
    'type': 'object',
    'required': ['id', 'rating', 'comment', 'tip_and_trick_id'],
    'additionalProperties': False,
    'properties': {
        'id': {'type': 'integer'},
        'rating': {'type': 'integer'},
        'comment': {'type': 'string'},
        'tip_and_trick_id': {'type': 'integer'},
    },
}

schema_tip_and_trick_rating_put = {
    'type': 'object',
    'required': ['rating', 'comment', 'tip_and_trick_id'],
    'additionalProperties': False,
    'properties': {
        'rating': {'type': 'integer'},
        'comment': {'type': 'string'},
        'tip_and_trick_id': {'type': 'integer'},
    },
}

schema_category_post = {
    'type': 'object',
    'required': ['id', 'title', 'description'],
    'additionalProperties': False,
    'properties': {
        'id': {'type': 'integer'},
        'title': {'type': 'string'},
        'description': {'type': 'string'},
    },
}

schema_category_put = {
    'type': 'object',
    'required': ['title', 'description'],
    'additionalProperties': False,
    'properties': {
        'title': {'type': 'string'},
        'description': {'type': 'string'},
    },
}

import time


def is_string_empty(value):
    return value == '' or value is None


def is_any_string_empty(values):
    for value in values:
        if is_string_empty(value):
            return True
    return False


def get_now():
    return int(time.time() * 1000)

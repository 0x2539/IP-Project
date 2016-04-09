import time


def is_string_empty(value):
    return value == '' or value is None


def get_now():
    return int(time.time() * 1000)

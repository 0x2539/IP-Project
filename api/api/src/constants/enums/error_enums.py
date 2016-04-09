from enum import Enum


class BadAuthEnum(Enum):
    WEAK_PASSWORD = 0
    AUTH_EXISTS = 1
    AUTH_BAD_FORMAT = 2
    WRONG_AUTH = 3
    WRONG_PASSWORD = 4
    EMPTY_PASSWORD = 5

from enum import Enum


class UserTypeEnum(Enum):
    # Keep difference of 10 so we can add more between them if necessary
    UNAUTHORIZED = 0
    NORMAL = 10
    MODERATOR = 20
    ADMIN = 30

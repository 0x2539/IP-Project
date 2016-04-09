

class BadAuthException(Exception):

    error = None  # BadAuthEnum()
    additional_object = None  # any object we want to pass with the exception

    def __init__(self, error, additional_object=None):
        self.error = error
        self.additional_object = additional_object

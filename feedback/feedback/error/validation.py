class ValidationException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

    def get_message(self):
        return self.message

    def get_code(self):
        return self.code

    def __str__(self):
        return self.message

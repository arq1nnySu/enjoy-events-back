
class ValidationError(Exception):
    def __init__(self):
        self.message = "This field can't be empty."
        self.error_code = 400


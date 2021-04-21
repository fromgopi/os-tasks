#pylint: disable=missing-final-newline
""" All API Exceptions"""

class ApiError(Exception):
    """
    Custom API Exception
    """
    def __init__(self, status, message, errors=None):
        super().__init__(message)
        self.status = status
        self.message = message
        if errors:
            self.errors = errors
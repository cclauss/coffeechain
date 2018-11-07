from rest_framework.exceptions import APIException


class Api400(APIException):
    """
    Custom api exception which supports:
    - custom message
    - custom error code
    - optional 'details' dict of arbitrary data to help debugging
    """

    def __init__(self, message, code=0, details=None):
        self.status_code = 400
        self.detail = {
            "error": message,
            "error_code": code,
            "details": details or {}
        }

from django.core.exceptions import ValidationError

from rest_framework.exceptions import APIException, _get_error_details


class CustomAPIExceptionError(APIException):
    default_detail = 'Error'
    default_code = 400

    def __init__(self, code: int = None, detail: str | dict | list | tuple = None) -> None:
        if detail is None:
            detail = self.default_detail
        if code is None:
            code = self.default_code

        if isinstance(detail, tuple):
            detail = list(detail)
        elif not isinstance(detail, dict) and not isinstance(detail, list):
            detail = [detail]

        self.detail = _get_error_details(detail, code)
        

class CustomExceptionError(Exception):
    pass
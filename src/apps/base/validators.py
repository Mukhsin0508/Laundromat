import uuid

from django.core.validators import BaseValidator
from apps.base.exceptions import CustomExceptionError


class CustomBaseValidator(BaseValidator):
    pass




def validate_uuid(value):
    try:
        uuid.UUID(str(value))
    except ValueError:
        raise CustomExceptionError(code=400, detail={'error': f'{value} is not UUID'})
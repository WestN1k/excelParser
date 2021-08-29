import os
from django.core.exceptions import ValidationError


def file_validate(file):
    ext = os.path.splitext(file.name)[1]
    valid_extensions = ['.xls', '.xlsx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

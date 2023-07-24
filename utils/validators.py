from django.core import validators, exceptions


def is_valid_url(url: str) -> bool:
    validator = validators.URLValidator()

    if not isinstance(url, str):
        "Check if url is string not object or any."
        return False

    try:
        validator(url)
        return True
    except exceptions.ValidationError:
        return False

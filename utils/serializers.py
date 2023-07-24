from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers


class StringPrimaryKeyRelateField(serializers.RelatedField):
    default_error_messages = {
        'required': 'This field is required.',
        'does_not_exist': 'Invalid pk "{pk_value}" - object does not exist.',
        'incorrect_type': 'Incorrect type. Expected pk value, received {data_type}.',
    }

    def to_internal_value(self, data):
        queryset = self.get_queryset()
        try:
            if isinstance(data, bool):
                raise TypeError
            return queryset.get(pk=data)
        except ObjectDoesNotExist:
            self.fail('does_not_exist',
                      pk_value=data)
        except (TypeError, ValueError):
            self.fail(
                'incorrect_type', data_type=type(data).__name__)

    def to_representation(self, value):
        return str(value)

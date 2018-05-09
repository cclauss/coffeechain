"""
Fields used for specific reason by this API
----
./drf/fields.py - generic fields with different functionality
"""
from rest_framework import fields, serializers

from coffeechain.proto import address
from coffeechain.utils.drf.validation import sawtooth_address_exists, sawtooth_address_doesnt_exist


def _add_validator(kwargs, key_func=None, exists=False):
    if not hasattr(address, key_func):
        raise Exception("coffeechain.proto.address does not have function %s" % key_func)

    current = kwargs.pop("validators", [])
    func = sawtooth_address_exists if exists else sawtooth_address_doesnt_exist
    current.append(func(key_func))
    kwargs['validators'] = current


class KeyField(fields.SlugField):
    def __init__(self, key_func=None, exists=False, **kwargs):
        if key_func:
            _add_validator(kwargs, key_func=key_func, exists=exists)
        kwargs.setdefault("required", True)
        kwargs.setdefault("min_length", 4)
        kwargs.setdefault("max_length", 32)
        super().__init__(**kwargs)


class NameField(fields.CharField):
    def __init__(self, **kwargs):
        kwargs.setdefault("min_length", 4)
        kwargs.setdefault("max_length", 128)
        super().__init__(**kwargs)


class LocationSerializer(serializers.Serializer):
    lat = fields.FloatField(required=True)
    lng = fields.FloatField(required=True)
    description = NameField(required=True)


class KeyListField(serializers.ListField):
    def __init__(self, key_func=None, exists=True, **kwargs):
        kwargs.setdefault('child', KeyField(required=False, key_func=key_func, exists=exists))
        kwargs.setdefault('required', False)
        kwargs.setdefault('default', list)
        super().__init__(**kwargs)

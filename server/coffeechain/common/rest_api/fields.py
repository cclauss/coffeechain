"""
Fields used for specific reason by this API.
Designed to be used with import *
----
./drf/fields.py - generic fields with different functionality
"""
# prefix with _ to keep hidden from import *
from rest_framework import serializers as _serializers
# noinspection PyUnresolvedReferences
from rest_framework.fields import (
    # import all the fields we want to add to "import *"
    BooleanField, CharField, ChoiceField, DateField, DateTimeField, DecimalField, DictField,
    DurationField, EmailField, Field, FileField, FilePathField, FloatField, HStoreField, HiddenField,
    IPAddressField, ImageField, IntegerField, JSONField, ListField, ModelField, MultipleChoiceField,
    NullBooleanField, ReadOnlyField, RegexField, SerializerMethodField, SlugField, TimeField,
    URLField, UUIDField
)
# noinspection PyUnresolvedReferences
from coffeechain.utils.drf.fields import (
    ArrowDateTimeField, JsonSchemaField, LatLngField, ConstantField,
    LowerCaseEmailField, UnixTimeField
)


class KeyField(SlugField):
    def __init__(self, key_func=None, exists=False, **kwargs):
        if key_func:
            _add_validator(kwargs, key_func=key_func, exists=exists)
        kwargs.setdefault("required", True)
        kwargs.setdefault("min_length", 4)
        kwargs.setdefault("max_length", 32)
        super().__init__(**kwargs)


class NameField(CharField):
    def __init__(self, **kwargs):
        kwargs.setdefault("min_length", 4)
        kwargs.setdefault("max_length", 128)
        super().__init__(**kwargs)


class LocationField(_serializers.Serializer):
    lat = FloatField(required=True)
    lng = FloatField(required=True)
    description = NameField(required=True)


class KeyListField(_serializers.ListField):
    def __init__(self, key_func=None, exists=True, **kwargs):
        kwargs.setdefault('child', KeyField(required=False, key_func=key_func, exists=exists))
        kwargs.setdefault('required', False)
        kwargs.setdefault('default', list)
        super().__init__(**kwargs)


def _add_validator(kwargs, key_func=None, exists=False):
    from coffeechain.proto import address as address
    from coffeechain.utils.drf.validation import sawtooth_address_exists, sawtooth_address_doesnt_exist

    if not hasattr(address, key_func):
        raise Exception("coffeechain.proto.address does not have function %s" % key_func)

    current = kwargs.pop("validators", [])
    func = sawtooth_address_exists if exists else sawtooth_address_doesnt_exist
    current.append(func(key_func))
    kwargs['validators'] = current

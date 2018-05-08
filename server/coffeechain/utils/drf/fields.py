# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, unicode_literals

import decimal
import logging

import arrow
import django
import jsonschema
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_text
from django.utils.formats import sanitize_separators
from rest_framework import serializers

logger = logging.getLogger(__name__)


class JsonSchemaField(serializers.JSONField):

    def __init__(self, schema=None, **kwargs):
        assert schema is not None, "Schema is required"
        super(JsonSchemaField, self).__init__(**kwargs)
        self.schema = schema

    def to_internal_value(self, data):
        data = super(JsonSchemaField, self).to_internal_value(data)
        try:
            jsonschema.validate(data, self.schema)
        except Exception as e:
            raise serializers.ValidationError(e.message)
        return data


class LatLngField(serializers.DecimalField):
    def __init__(self, **kwargs):
        super(LatLngField, self).__init__(max_digits=10, decimal_places=7, **kwargs)

    def to_internal_value(self, data):
        """
        Validate that the input is a decimal number and return a Decimal
        instance. Truncates the value to 7 decimals.
        """
        data = smart_text(data).strip()

        if self.localize:
            data = sanitize_separators(data)

        if len(data) > self.MAX_STRING_LENGTH:
            self.fail('max_string_length')

        try:
            value = decimal.Decimal(data)
        except decimal.DecimalException:
            self.fail('invalid')

        # Check for NaN. It is the only value that isn't equal to itself,
        # so we can use this to identify NaN values.
        if value != value:
            self.fail('invalid')

        # Check for infinity and negative infinity.
        if value in (decimal.Decimal('Inf'), decimal.Decimal('-Inf')):
            self.fail('invalid')

        # Truncate the value if needed
        max_exp = self.decimal_places
        s, d, e = value.as_tuple()
        if abs(e) > max_exp:
            d = d[:e] + d[e:][:max_exp]
            value = decimal.Decimal([s, d, -max_exp])

        return self.quantize(self.validate_precision(value))


class UnixTimeField(serializers.Field):
    """
    Represents a UTC unix timestamp.
    - Receives data as an integer
    - Converts python object (usually a datetime) and sends a utc timestamp (via utctimetuple() in arrow)
    """

    def to_representation(self, obj):
        return arrow.get(obj).timestamp

    def to_internal_value(self, data):
        return arrow.get(int(data)).datetime


def value_to_lower(v):
    return v.lower() if v else v


class LowerCaseEmailField(serializers.EmailField):
    def to_internal_value(self, value):
        value = super(LowerCaseEmailField, self).to_internal_value(value)
        return value.lower() if value else value

    def to_representation(self, value):
        value = super(LowerCaseEmailField, self).to_representation(value)
        return value.lower() if value else value


class ConstantField(serializers.ReadOnlyField):
    """
    Read-only field which always returns the constant value supplied.
    """
    constant_value = None

    def __init__(self, value=None):
        super(ConstantField, self).__init__()
        self.constant_value = value

    def get_attribute(self, instance):
        """
        DRF Says: Given the *outgoing* object instance, return the primitive value
        that should be used for this field.
        We Say:   Ignore the instance, just return the constant
        """
        return self.constant_value


class ArrowDateTimeField(serializers.Field):
    """
    A date time field that uses the arrow library for better parsing, and parsing of more formats.

    - input is parsed using arrow.get()
    - output is always an ISO 8601 date string
    """

    default_error_messages = {
        'invalid_value': 'Unable to convert "{value}" to a datetime ({exc})'
    }

    def __init__(self, as_str=False, **kwargs):
        super(ArrowDateTimeField, self).__init__(**kwargs)
        self.as_str = as_str

    def to_internal_value(self, value):
        try:
            arr = arrow.get(value)
            return str(arr) if self.as_str else arr.datetime
        except Exception as e:
            self.fail('invalid_value', value=value, exc=str(e))

    def to_representation(self, value):
        if not value:
            return None
        return str(arrow.get(value))


def get_model_field_names(model_class):
    # noinspection PyProtectedMember
    if django.VERSION >= (1, 10):
        from itertools import chain
        return list(set(chain.from_iterable(
            (field.name, field.attname) if hasattr(field, 'attname') else (field.name,)
            for field in model_class._meta.get_fields()
            # For complete backwards compatibility, you may want to exclude
            # GenericForeignKey from the results.
            if not (field.many_to_one and field.related_model is None)
        )))
    else:
        return model_class._meta.get_all_field_names()

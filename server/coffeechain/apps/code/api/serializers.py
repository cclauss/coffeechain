from rest_framework import fields
from rest_framework.serializers import Serializer

from coffeechain.utils.drf.fields import ArrowDateTimeField


class MintCodesSerializer(Serializer):
    company = fields.IntegerField(required=True)
    messages = fields.ListField(
        required=True,
        child=fields.CharField(max_length=32, min_length=24)
    )
    created_at = ArrowDateTimeField(required=True, as_str=True)


class ActivateCodesSerializer(Serializer):
    messages = fields.ListField(
        required=True, min_length=1,
        child=fields.CharField(max_length=32, min_length=24)
    )
    activated_at = ArrowDateTimeField(required=True, as_str=True)

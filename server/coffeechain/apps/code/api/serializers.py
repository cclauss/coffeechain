from rest_framework import serializers

from coffeechain.common.rest_api.fields import *
from coffeechain.utils.drf.fields import ArrowDateTimeField


class MintCodesSerializer(serializers.Serializer):
    company = IntegerField(required=True)
    messages = ListField(
        required=True,
        child=CharField(max_length=32, min_length=24)
    )
    created_at = ArrowDateTimeField(required=True, as_str=True)


class ActivateCodesSerializer(serializers.Serializer):
    messages = ListField(
        required=True, min_length=1,
        child=CharField(max_length=32, min_length=24)
    )
    activated_at = ArrowDateTimeField(required=True, as_str=True)

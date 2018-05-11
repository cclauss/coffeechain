from rest_framework import serializers

from coffeechain.common.rest_api.fields import *
from coffeechain.utils.drf.fields import ArrowDateTimeField


class MintCodesSerializer(serializers.Serializer):
    company = IntegerField(required=True)
    messages = KeyListField("for_code", exists=False)
    created_at = ArrowDateTimeField(required=True, as_str=True)


class ActivateCodesSerializer(serializers.Serializer):
    messages = KeyListField("for_code", exists=True)
    activated_at = ArrowDateTimeField(required=True, as_str=True)

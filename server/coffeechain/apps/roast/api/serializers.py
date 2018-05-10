from rest_framework import serializers

from coffeechain.common.rest_api.fields import *
from coffeechain.utils.drf.fields import ArrowDateTimeField


class RoastCreateSerializer(serializers.Serializer):
    key = KeyField("for_roast")
    roasted_at = ArrowDateTimeField(required=True, as_str=True)
    location = LocationField(required=True)
    harvests = KeyListField("for_harvest")


class RoastAddHarvestSerializer(serializers.Serializer):
    key = KeyField("for_harvest", exists=True)

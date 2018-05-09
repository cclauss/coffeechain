from rest_framework import serializers

from coffeechain.utils import api_fields
from coffeechain.utils.api_fields import LocationSerializer
from coffeechain.utils.drf.fields import ArrowDateTimeField


class RoastCreateSerializer(serializers.Serializer):
    key = api_fields.KeyField("for_roast")
    roasted_at = ArrowDateTimeField()
    location = LocationSerializer(required=True)
    harvests = api_fields.KeyListField("for_harvest")


class RoastAddHarvestSerializer(serializers.Serializer):
    key = api_fields.KeyField("for_harvest")

from rest_framework import serializers

from coffeechain.utils import api_fields
from coffeechain.utils.drf.fields import ArrowDateTimeField


class ShipmentCreateSerializer(serializers.Serializer):
    key = api_fields.KeyField("for_harvest", exists=False)
    source = api_fields.LocationSerializer()
    destination = api_fields.LocationSerializer()
    shipped_at = ArrowDateTimeField(as_str=True)
    recieved_at = ArrowDateTimeField(required=False, as_str=True)

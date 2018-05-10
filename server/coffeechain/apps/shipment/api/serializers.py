from rest_framework import serializers

from coffeechain.common.rest_api.fields import *
from coffeechain.utils.drf.fields import ArrowDateTimeField


class ShipmentCreateSerializer(serializers.Serializer):
    key = KeyField("for_harvest", exists=False)
    kg = IntegerField(default=0, min_value=0, max_value=100 * 1000)
    ship_name = CharField(max_length=100)
    source = LocationField()
    destination = LocationField()
    shipped_at = ArrowDateTimeField(required=False, as_str=True)
    recieved_at = ArrowDateTimeField(required=False, as_str=True)
    extra_info = ListField(child=CharField(max_length=500))

from rest_framework import serializers

from coffeechain.common.rest_api.fields import *


class CreateHarvestSerializer(serializers.Serializer):
    key = KeyField("for_harvest", exists=False)
    year = IntegerField(min_value=2017, max_value=2100)
    month = IntegerField(min_value=1, max_value=12)
    location = LocationField()
    farms = KeyListField("for_farm")
    shipments = KeyListField("for_shipment")


class AddFarmSerializer(serializers.Serializer):
    key = KeyField("for_farm", exists=True)


class AddShipmentSerializer(serializers.Serializer):
    key = KeyField("for_shipment", exists=True)

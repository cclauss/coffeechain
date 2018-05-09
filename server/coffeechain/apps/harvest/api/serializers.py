from rest_framework import serializers, fields

from coffeechain.utils import api_fields


class CreateHarvestSerializer(serializers.Serializer):
    key = api_fields.KeyField("for_harvest", exists=False)
    year = fields.IntegerField(min_value=2017, max_value=2100)
    month = fields.IntegerField(min_value=1, max_value=12)
    location = api_fields.LocationSerializer()
    farms = api_fields.KeyListField("for_farm")
    shipments = api_fields.KeyListField("for_shipment")


class AddFarmSerializer(serializers.Serializer):
    key = api_fields.KeyField("for_farm", exists=True)


class AddShipmentSerializer(serializers.Serializer):
    key = api_fields.KeyField("for_shipment", exists=True)

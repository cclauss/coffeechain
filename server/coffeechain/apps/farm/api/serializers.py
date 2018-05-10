from rest_framework import serializers

from coffeechain.common.rest_api.fields import *
from coffeechain.utils.drf.validation import sawtooth_address_exists, sawtooth_address_doesnt_exist


class CreateFarmSerializer(serializers.Serializer):
    key = KeyField(validators=[sawtooth_address_doesnt_exist("for_farm")])
    name = NameField()
    address = ListField(child=CharField(max_length=500))
    location = LocationField(required=True)
    certifications = KeyListField("for_cert")


class AddCertSerializer(serializers.Serializer):
    key = KeyField(validators=[sawtooth_address_exists("for_cert")])

from rest_framework import serializers, fields

from coffeechain.utils import api_fields
from coffeechain.utils.api_fields import LocationSerializer
from coffeechain.utils.drf.validation import sawtooth_address_exists, sawtooth_address_doesnt_exist


class CreateFarmSerializer(serializers.Serializer):
    key = api_fields.KeyField(validators=[sawtooth_address_doesnt_exist("for_farm")])
    name = api_fields.NameField()
    location = LocationSerializer(required=True)
    certifications = fields.ListField(
        required=False,
        child=api_fields.KeyField(required=False, validators=[sawtooth_address_exists("for_cert")]),
        default=list
    )


class AddCertSerializer(serializers.Serializer):
    key = api_fields.KeyField(validators=[sawtooth_address_exists("for_cert")])

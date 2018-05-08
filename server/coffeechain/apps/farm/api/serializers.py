from rest_framework import serializers, fields

from coffeechain.utils import sawtooth_fields
from coffeechain.utils.drf.validation import sawtooth_address_exists, sawtooth_address_doesnt_exist


class LocationSerializer(serializers.Serializer):
    lat = fields.FloatField(required=True)
    lng = fields.FloatField(required=True)
    description = sawtooth_fields.NameField(required=True)


class CreateFarmSerializer(serializers.Serializer):
    key = sawtooth_fields.KeyField(validators=[sawtooth_address_doesnt_exist("for_farm")])
    name = sawtooth_fields.NameField()
    location = LocationSerializer(required=True)
    certifications = fields.ListField(
        required=False,
        child=sawtooth_fields.KeyField(required=False, validators=[sawtooth_address_exists("for_cert")]),
        default=list
    )


class AddCertSerializer(serializers.Serializer):
    key = sawtooth_fields.KeyField(validators=[sawtooth_address_exists("for_cert")])

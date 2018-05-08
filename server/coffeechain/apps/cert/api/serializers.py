from rest_framework import serializers, fields


class CreateCertSerializer(serializers.Serializer):
    key = fields.SlugField(required=True, max_length=32, help_text="Key that is used to refer to this document")
    url = fields.URLField(required=True, max_length=1024, help_text="URL to the online certification document")
    name = fields.CharField(required=True, max_length=120)

from rest_framework import serializers, fields


class CreateCertSerializer(serializers.Serializer):
    key = fields.SlugField(max_length=32, help_text="Key that is used to refer to this document")
    url = fields.URLField(help_text="URL to the online certification document", max_length=1024)
    name = fields.CharField(max_length=120)

from rest_framework import fields
from rest_framework.serializers import Serializer


class MintCodesSerializer(Serializer):
    company = fields.IntegerField(required=True)
    messages = fields.ListField(
        required=True,
        child=fields.CharField(max_length=32, min_length=24)
    )

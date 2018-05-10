import hashlib

import requests
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from coffeechain.common.rest_api.fields import *


class HostedFileField(serializers.Serializer):
    """
    Takes a url & name field, downloads the file and computes the md5 hash & size
    """
    url = URLField(required=False)
    name = CharField(max_length=100)

    def validate(self, attrs):
        if not attrs['url']:
            return {}
        try:
            resp = requests.get(attrs['url'], timeout=10)
            if resp.status_code != 200:
                raise ValidationError({
                    "url": [
                        "Invalid url: %s" % attrs['url']
                    ]}, code="url")

            doc = resp.content
            attrs['md5_hash'] = hashlib.md5(doc).hexdigest()
            attrs['size']: len(doc)
        except ValidationError as e:
            raise
        except Exception as e:
            print("Error Downloading %s" % attrs['url'])
            print("   error: %s" % str(e))
            raise ValidationError(detail={
                "url": [
                    "Error downloading and verifying the cetificate",
                    "%s" % e
                ]}, code="url")

        return attrs


class CreateCertSerializer(serializers.Serializer):
    key = KeyField("for_cert", help_text="Key that is used to refer to this document")
    certifier_url = URLField(required=True, max_length=1024, help_text="URL to the online certification document")
    name = CharField(required=True, max_length=120)
    instructions = CharField(max_length=1000)
    valid_from = ArrowDateTimeField(required=False, as_str=True)
    valid_to = ArrowDateTimeField(required=True, as_str=True)
    file = HostedFileField()

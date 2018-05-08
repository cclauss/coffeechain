import hashlib

import requests
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from coffeechain.apps.cert.api import serializers
from coffeechain.proto import address
from coffeechain.proto.coffee_pb2 import CoffeeChainEvents, Certification
from coffeechain.services import sawtooth_api
from coffeechain.utils.drf.validation import validate_using


class CreateCertView(APIView):
    def post(self, request, *args, **kwargs):
        data = validate_using(serializers.CreateCertSerializer, data=request.data, view=self)
        cert_address = address.hash(data['key'])

        if sawtooth_api.state_exists(cert_address):
            raise ValidationError({"key": "Cert already exists at that address"})

        try:
            doc = requests.get(data['url'], timeout=10).content
        except Exception as e:
            return Response(status=400, data={
                "error": "Error downloading and verifying the cetificate",
                "details": {
                    "message": str(e),
                }
            })

        new_cert = Certification(
            key=data['key'],
            name=data['name'],
            url=data['url'],
            hash=hashlib.md5(doc).hexdigest(),
            size=len(doc)
        )
        
        resp_json = sawtooth_api.submit_batch(
            sawtooth_api.create_txn(
                CoffeeChainEvents(cert_create=new_cert),
                outputs=[cert_address]
            )
        )

        return Response(data=resp_json)


class GetCertView(APIView):

    def get(self, request, key=""):
        cert_address = address.hash(key)
        err, cert = sawtooth_api.get_state_as(Certification, cert_address)

        if err:
            return Response(status=400, data={
                "error": "Error getting certification",
                "details": {
                    "error_code": err,
                    "address": cert_address
                }
            })

        return Response(
            data=sawtooth_api.proto_to_dict(cert)
        )

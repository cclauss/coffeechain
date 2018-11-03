from rest_framework.response import Response
from rest_framework.views import APIView

from coffeechain.apps.cert.api import serializers
from coffeechain.proto import address
from coffeechain.proto.coffee_pb2 import Certification
from coffeechain.services import sawtooth_api
from coffeechain.utils.drf.validation import validate_using
from coffeechain.utils.misc import check_bigchaindb_enable

from coffeechain.services import bigchaindb_api

class CreateCertView(APIView):
    def post(self, request, *args, **kwargs):
        data = validate_using(serializers.CreateCertSerializer, data=request.data, view=self)
        if(check_bigchaindb_enable()):
            resp_json = bigchaindb_api.create(data)
        else:
            new_cert = Certification(**data)
            resp_json = sawtooth_api.submit_event(
            cert_create=new_cert,
            outputs=[address.for_cert(new_cert.key)])
        
        return Response(resp_json)


class GetCertView(APIView):

    def get(self, request, key=""):
        if(check_bigchaindb_enable()):
            data = bigchaindb_api.search_asset(key)[0]['data']
        else:
            cert_address = address.for_cert(key)
            err, cert = sawtooth_api.get_state_as(Certification, cert_address)

            if err:
                return Response(status=400, data={
                "error": "Error getting certification",
                    "details": {
                    "error_code": err,
                    "address": cert_address
                }
            })
            data=sawtooth_api.proto_to_dict(cert)

        return Response(data)

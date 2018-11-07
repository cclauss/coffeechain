from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from coffeechain.apps.cert.api import serializers
from coffeechain.common.constants import Chain
from coffeechain.proto import address
from coffeechain.proto.coffee_pb2 import Certification
from coffeechain.services import sawtooth_api, bigchaindb_api
from coffeechain.utils.drf.exceptions import Api400
from coffeechain.utils.drf.validation import validate_using
from coffeechain.utils.multi_chain import MultiChain, chain_, get_for_chain


class CreateCertView(APIView):
    def post(self, request: Request):
        data = validate_using(serializers.CreateCertSerializer, data=request.data, view=self)
        return Response(
            # demonstrates using the class based MultiChain object to run chain-specific code
            data=self.CreateCert(**data)
        )

    class CreateCert(MultiChain):
        def bigchain(self, *args, **kwargs):
            return bigchaindb_api.create(kwargs)

        def sawtooth(self, *args, **kwargs):
            new_cert = Certification(**kwargs)
            return sawtooth_api.submit_event(
                cert_create=new_cert,
                outputs=[address.for_cert(new_cert.key)]
            )


class GetCertView(APIView):

    def get(self, request: Request, key: str = ""):
        # demonstrates using anotehr method of getting chain specific functionality
        f = get_for_chain(
            self.bigchain,
            self.sawtooth
        )
        return Response(f(key=key))

    @chain_(Chain.BIGCHAIN)
    def bigchain(self, key):
        errmsg, data = bigchaindb_api.find_one(key)
        if errmsg:
            raise Api400(message=errmsg, details={
                'key': key,
                'bigchain': data
            })
        return data

    @chain_(Chain.SAWTOOTH)
    def sawtooth(self, key):
        cert_address = address.for_cert(key)
        err, cert = sawtooth_api.get_state_as(Certification, cert_address)
        if err:
            raise Api400(message="Error getting certificate", details={
                'key': key,
                'sawtooth': dict(
                    error_code=err,
                    address=cert_address
                )
            })
        return sawtooth_api.proto_to_dict(cert)

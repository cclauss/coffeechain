import requests
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from coffeechain.apps.cert.api import serializers
from coffeechain.apps.data.models import RequestLog, ChainBatch
from coffeechain.proto import address
from coffeechain.proto.coffee_pb2 import Certification
from coffeechain.services import sawtooth_api
from coffeechain.utils.drf.validation import validate_using


class CreateCertView(APIView):
    def post(self, request, *args, **kwargs):
        data = validate_using(serializers.CreateCertSerializer, data=request.data, view=self)

        t = log_request(request, data, "cert", "create")
        new_cert = Certification(**data)
        resp_json = sawtooth_api.submit_event(
            cert_create=new_cert,
            outputs=[address.for_cert(new_cert.key)]
        )

        # batch submit always comes back with a link to the batch status
        if 'link' in resp_json:
            batch_resp = requests.get(resp_json['link'])
            batch_data = batch_resp['data']
            batch = ChainBatch.objects.create(
                batch_id=batch_data['id'],
                batch_status=batch_data['status']
            )

        return Response(data=resp_json)


class GetCertView(APIView):

    def get(self, request, key=""):
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

        return Response(
            data=sawtooth_api.proto_to_dict(cert)
        )


def log_request(request: Request, data, object_type, action):
    return RequestLog.objects.create(
        url=request.META.get("PATH_INFO", ""),
        content=request.data,
        type=object_type,
        action=action,
    )

from functools import partial

from google.protobuf.json_format import MessageToJson
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from coffeechain.proto import address
from coffeechain.proto.coffee_pb2 import CoffeeChainEvents, Events
from coffeechain.services import sawtooth_api
from coffeechain.utils.drf.validation import validate_using
from . import serializers


def _txn(name, cls, inputs=None, outputs=None, **kwargs):
    return sawtooth_api.create_txn(
        obj=CoffeeChainEvents(**{name: cls(**kwargs)}),
        inputs=inputs or [],
        outputs=outputs or []
    )


mint_code = partial(_txn, "mint_code", Events.MintCode)
activate_code = partial(_txn, "activate_code", Events.ActivateCode)


class MintCodes(APIView):
    def post(self, request, *args):
        """
        Registers a list of codess with the same created_at and company_id
        """
        data = validate_using(serializers.MintCodesSerializer, data=request.data)

        resp = sawtooth_api.submit_batch([
            mint_code(message=msg, created_at=data['created_at'], outputs=[address.for_code(msg)])
            for msg in data['message']
        ])

        return Response(data=resp)


class ActivateCodesView(APIView):
    def post(self, request):
        data = validate_using(serializers.ActivateCodesSerializer, data=request.data)

        resp = sawtooth_api.submit_batch([
            activate_code(message=msg, activated_at=data['activated_at'],
                          inputs=[address.for_code(msg)],
                          outputs=[address.for_code(msg)])
            for msg in data['messages']
        ])

        return Response(data=resp)


class GetCode(APIView):
    def get(self, request, *args, **kwargs):
        assert 'message' in kwargs
        print(address.for_code("message-xyzabc123youassholeserializethis"))
        code = sawtooth_api.get_code(kwargs['message'])
        return Response(
            data={
                "type": "code",
                "data": json.loads(MessageToJson(code))
            }
        )

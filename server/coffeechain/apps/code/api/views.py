import requests
from google.protobuf.json_format import MessageToJson
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from sawtooth_sdk.protobuf.transaction_pb2 import Transaction

from coffeechain.proto import address
from coffeechain.proto.coffee_pb2 import CoffeeChainEvents, Events
from coffeechain.services import sawtooth_api
from coffeechain.utils.drf.validation import validate_using
from . import serializers


class MintCodes(APIView):
    def post(self, request, *args):
        """
        Registers a list of codess
        """
        data = validate_using(serializers.MintCodesSerializer, data=request.data)

        txns = []
        for msg in data['messages']:
            txns.append(sawtooth_api.create_txn(
                obj=CoffeeChainEvents(mint_code=Events.MintCode(message=msg)),
                outputs=[address.for_code(msg)]
            ))

        resp = sawtooth_api.submit_batch(txns)

        return Response(
            data=resp
        )


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

from functools import partial

from rest_framework.response import Response
from rest_framework.views import APIView

from coffeechain.proto import address
from coffeechain.proto.coffee_pb2 import Events, Code
from coffeechain.services import sawtooth_api
from coffeechain.services.sawtooth_api import event_transaction
from coffeechain.utils.drf.validation import validate_using
from . import serializers

mint_code = partial(event_transaction, "mint_code", Events.MintCode)
activate_code = partial(event_transaction, "activate_code", Events.ActivateCode)


class MintCodes(APIView):
    def post(self, request, *args):
        """
        Registers a list of codess with the same created_at and company_id
        """
        data = validate_using(serializers.MintCodesSerializer, data=request.data)

        resp = sawtooth_api.submit_batch([
            mint_code(
                message=msg,
                company=data['company'],
                created_at=data['created_at'],
                outputs=[address.for_code(msg)]
            )
            for msg in data['messages']
        ])

        return Response(data=resp)


class ActivateCodesView(APIView):
    def post(self, request):
        data = validate_using(serializers.ActivateCodesSerializer, data=request.data)

        resp = sawtooth_api.submit_batch([
            activate_code(
                message=msg,
                activated_at=data['activated_at'],
                inputs=[address.for_code(msg)],
                outputs=[address.for_code(msg)]
            )
            for msg in data['messages']
        ])

        return Response(data=resp)


class GetCode(APIView):
    def get(self, request, message):
        code = sawtooth_api.get_or_404(Code, address.for_code(message))
        return Response(sawtooth_api.proto_to_dict(code))

from rest_framework.response import Response
from rest_framework.views import APIView

from coffeechain.apps.shipment.api.serializers import ShipmentCreateSerializer
from coffeechain.proto import address
from coffeechain.proto.coffee_pb2 import *
from coffeechain.services import sawtooth_api
from coffeechain.utils.drf.validation import validate_using


class ShipmentCreateView(APIView):

    def post(self, request):
        # the output of validate_using should match the data format of the
        # Shipment object exactly
        data = validate_using(ShipmentCreateSerializer, data=request.data, view=self)
        shipment = Shipment(**data)
        resp = sawtooth_api.submit_event(
            shipment_create=shipment,
            inputs=[],
            outputs=[address.for_shipment(shipment.key)]
        )
        return Response(data=resp)


class ShipmentGetView(APIView):
    def get(self, request, key=None):
        harvest = sawtooth_api.get_or_404(Shipment, address.for_harvest(key))
        return Response(data=sawtooth_api.proto_to_dict(harvest))

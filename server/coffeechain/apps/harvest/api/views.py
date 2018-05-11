from rest_framework.response import Response
from rest_framework.views import APIView

from coffeechain.apps.harvest.api.serializers import CreateHarvestSerializer, AddShipmentSerializer, AddFarmSerializer
from coffeechain.proto import address
from coffeechain.proto.coffee_pb2 import *
from coffeechain.services import sawtooth_api
from coffeechain.utils.drf.validation import validate_using


class HarvestCreateView(APIView):

    def post(self, request):
        data = validate_using(CreateHarvestSerializer, data=request.data, view=self)
        harvest = Harvest(**data)

        resp = sawtooth_api.submit_event(
            harvest_create=harvest,
            inputs=(
                [address.for_farm(f) for f in harvest.farms] +
                [address.for_shipment(s) for s in harvest.shipments]
            ),
            outputs=[address.for_harvest(harvest.key)],
        )

        return Response(
            data=resp
        )


class HarvestGetView(APIView):
    def get(self, request, key=None):
        harvest = sawtooth_api.get_or_404(Harvest, address.for_harvest(key))
        return Response(data=sawtooth_api.proto_to_dict(harvest))


class HarvestAddFarmView(APIView):
    def post(self, request, key):
        harvest = sawtooth_api.get_or_404(Harvest, address.for_harvest(key))
        data = validate_using(AddFarmSerializer, data=request.data, view=self)

        resp = sawtooth_api.submit_event(
            add_related=Events.AddRelated(
                action="harvest_farm",
                object_key=key,  # key from the URL, already validated
                related_key=data['key']  # key from the post-data, already validated
            ),
            inputs=[address.for_harvest(key), address.for_farm(data['key'])],
            outputs=[address.for_harvest(key)]  # this is the address we will be writing to
        )

        return Response(data=resp)


class HarvestAddShipmentView(APIView):
    def post(self, request, key):
        harvest = sawtooth_api.get_or_404(Harvest, address.for_harvest(key))
        data = validate_using(AddShipmentSerializer, data=request.data, view=self)

        resp = sawtooth_api.submit_event(
            add_related=Events.AddRelated(
                action="harvest_shipment",
                object_key=key,  # key from the URL, already validated
                related_key=data['key']  # key from the post-data, already validated
            ),
            inputs=[address.for_harvest(key), address.for_shipment(data['key'])],
            outputs=[address.for_harvest(key)]  # this is the address we will be writing to
        )

        return Response(data=resp)

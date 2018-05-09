from rest_framework.response import Response
from rest_framework.views import APIView

from coffeechain.apps.harvest.api.serializers import CreateHarvestSerializer, AddShipmentSerializer, AddFarmSerializer
from coffeechain.proto import address
from coffeechain.proto.coffee_pb2 import *
from coffeechain.services import sawtooth_api
from coffeechain.utils.drf.validation import validate_using


class CreateHarvestView(APIView):

    def post(self, request):
        data = validate_using(CreateHarvestSerializer, data=request.data, view=self)

        harvest = Harvest(
            key=data['key'],
            year=data['year'],
            month=data['month'],
            location=data['location'],
            farms=data['farms'],
            shipments=data['shipments']
        )

        resp = sawtooth_api.submit_batch(
            sawtooth_api.create_txn(
                obj=harvest,
                inputs=(
                    [address.for_farm(f) for f in harvest.farms] +
                    [address.for_shipment(s) for s in harvest.shipments]
                ),
                outputs=[address.for_harvest(harvest.key)]
            )
        )

        return Response(
            data=resp
        )


class GetHarvestView(APIView):
    def get(self, request, key=None):
        harvest = sawtooth_api.get_or_404(Harvest, address.for_harvest(key))
        return Response(data=sawtooth_api.proto_to_dict(harvest))


class AddFarmView(APIView):
    def post(self, request, key):
        harvest = sawtooth_api.get_or_404(Harvest, address.for_harvest(key))
        farm = validate_using(AddFarmSerializer, data=request.data, view=self)

        resp = sawtooth_api.submit_batch(
            sawtooth_api.create_txn(
                obj=CoffeeChainEvents(add_related=Events.AddRelated(
                    action="harvest_cert",
                    object_key=key,  # key from the URL, already validated
                    related_key=farm['key']  # key from the post-data, already validated
                )),
                inputs=[address.for_harvest(key), address.for_farm(farm['key'])],
                outputs=[address.for_harvest(key)]  # this is the address we will be writing to
            )
        )

        return Response(
            data=resp
        )


class AddShipmentView(APIView):
    def post(self, request, key):
        harvest = sawtooth_api.get_or_404(Harvest, address.for_harvest(key))
        shipment = validate_using(AddShipmentSerializer, data=request.data, view=self)

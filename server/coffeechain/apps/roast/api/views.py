from rest_framework.response import Response
from rest_framework.views import APIView

from coffeechain.apps.roast.api.serializers import RoastAddHarvestSerializer, RoastCreateSerializer
from coffeechain.proto import address
from coffeechain.proto.coffee_pb2 import Farm, Events, Roast, Harvest, Certification, Shipment
from coffeechain.services import sawtooth_api
from coffeechain.utils.drf.validation import validate_using


class RoastCreateView(APIView):
    def post(self, request, *args, **kwargs):
        data = validate_using(RoastCreateSerializer, data=request.data, view=self)
        roast = Roast(**data)

        resp = sawtooth_api.submit_event(
            roast_create=roast,
            inputs=[address.for_harvest(h) for h in roast.harvests],
            outputs=[address.for_roast(roast.key)]  # this is the address we will be writing to
        )

        return Response(data=resp)


class RoastGetView(APIView):
    def get(self, request, key=None):
        roast = sawtooth_api.get_or_404(Roast, address.for_roast(key))
        data = sawtooth_api.proto_to_dict(roast)

        sawtooth_api.resolve_keys(data, 'harvests', Harvest)
        for h in data['harvests']:
            sawtooth_api.resolve_keys(h, 'shipments', Shipment)
            sawtooth_api.resolve_keys(h, 'farms', Farm)
            for f in h['farms']:
                sawtooth_api.resolve_keys(f, 'certifications', Certification)

        return Response(
            data=data
        )


class RoastAddHarvestView(APIView):
    def post(self, request, key=None):
        roast = sawtooth_api.get_or_404(Roast, address.for_roast(key))
        data = validate_using(RoastAddHarvestSerializer, data=request.data, view=self)

        resp = sawtooth_api.submit_event(
            add_related=Events.AddRelated(
                action="roast_harvest",
                object_key=key,
                related_key=data['key']
            ),
            inputs=[address.for_harvest(data['key'])],
            outputs=[address.for_roast(key)]
        )

        return Response(data=resp)

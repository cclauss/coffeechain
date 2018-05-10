from rest_framework.response import Response
from rest_framework.views import APIView

from coffeechain.apps.farm.api.serializers import CreateFarmSerializer, AddCertSerializer
from coffeechain.proto import address
from coffeechain.proto.coffee_pb2 import Farm, Events, Certification
from coffeechain.services import sawtooth_api
from coffeechain.utils.drf.validation import validate_using


class CreateFarmView(APIView):
    def post(self, request, *args, **kwargs):
        data = validate_using(CreateFarmSerializer, data=request.data, view=self)
        farm = Farm(**data)
        resp = sawtooth_api.submit_event(
            farm_create=farm,
            inputs=[address.for_cert(c) for c in farm.certifications],
            outputs=[address.for_farm(data['key'])]  # this is the address we will be writing to
        )
        return Response(data=resp)


class AddCertView(APIView):
    def post(self, request, key):
        farm = sawtooth_api.get_or_404(Farm, address.for_farm(key))
        data = validate_using(AddCertSerializer, data=request.data, view=self)

        resp = sawtooth_api.submit_event(
            add_related=Events.AddRelated(
                action="farm_cert",
                object_key=key,
                related_key=data['key']
            ),
            inputs=[address.for_farm(data['key'])],  # farm  key is in the url
            outputs=[address.for_farm(key)]
        )

        return Response(data=resp)


class FarmGetView(APIView):
    def get(self, request, key=None):
        farm = sawtooth_api.get_or_404(Farm, address.for_farm(key))
        data = sawtooth_api.proto_to_dict(farm)
        sawtooth_api.resolve_keys(data, 'certifications', Certification)

        return Response(
            data=data
        )

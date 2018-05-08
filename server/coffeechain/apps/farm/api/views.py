from rest_framework.response import Response
from rest_framework.views import APIView

from coffeechain.apps.farm.api.serializers import CreateFarmSerializer, AddCertSerializer
from coffeechain.proto import address
from coffeechain.proto.coffee_pb2 import Farm, Events
from coffeechain.services import sawtooth_api
from coffeechain.utils.drf.validation import validate_using


class CreateFarmView(APIView):
    def post(self, request, *args, **kwargs):
        data = validate_using(CreateFarmSerializer, data=request.data, view=self)

        print(data)

        farm = Farm()
        farm.key = data['key']
        farm.name = data['name']
        farm.location.lat = data['location']['lat']
        farm.location.lng = data['location']['lng']
        farm.location.description = data['location']['description']

        print("%r" % farm)

        resp = sawtooth_api.submit_batch(
            sawtooth_api.create_txn(
                obj=farm,
                # need the certifications to exist
                inputs=[address.for_cert(c) for c in data['certifications']],
                # this is the address we will be writing to
                outputs=[address.for_farm(data['key'])]
            )
        )

        return Response(data=resp)


class AddCertView(APIView):
    def post(self, request, *args, **kwargs):
        data = validate_using(AddCertSerializer, data=request.data, view=self)

        resp = sawtooth_api.submit_batch(
            sawtooth_api.event_transaction(
                "farm_add_cert", Events.FarmAddCert,
                key=data['key'],
                inputs=[address.for_farm(kwargs['key'])]  # farm  key is in the url
            )
        )

        return Response(data=resp)

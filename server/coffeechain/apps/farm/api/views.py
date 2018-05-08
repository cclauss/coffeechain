from rest_framework.response import Response
from rest_framework.views import APIView

from coffeechain.apps.farm.api.serializers import CreateFarmSerializer, AddCertSerializer
from coffeechain.proto import address
from coffeechain.proto.coffee_pb2 import Farm, Events, CoffeeChainEvents, Certification
from coffeechain.services import sawtooth_api
from coffeechain.utils.drf.validation import validate_using


class CreateFarmView(APIView):
    def post(self, request, *args, **kwargs):
        data = validate_using(CreateFarmSerializer, data=request.data, view=self)

        farm = Farm()
        farm.key = data['key']
        farm.name = data['name']
        farm.location.lat = data['location']['lat']
        farm.location.lng = data['location']['lng']
        farm.location.description = data['location']['description']
        farm.certifications.extend(data.get('certifications', []))

        resp = sawtooth_api.submit_batch(
            sawtooth_api.create_txn(
                obj=CoffeeChainEvents(farm_create=farm),
                inputs=[address.for_cert(c) for c in farm.certifications],
                outputs=[address.for_farm(data['key'])]  # this is the address we will be writing to
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


class GetFarmView(APIView):
    def get(self, request, **kwargs):
        farm_address = address.for_farm(kwargs.get('key', None))
        err, farm = sawtooth_api.get_state_as(Farm, farm_address)

        if err:
            return Response(status=400, data={
                "error": "Error getting Farm",
                "details": {
                    "error_code": err,
                    "address": farm_address
                }
            })

        data = sawtooth_api.proto_to_dict(farm)

        def _get_cert(key):
            cert_address = address.for_cert(key)
            err, cert = sawtooth_api.get_state_as(Certification, cert_address)
            if err:
                cert = Certification(key=key, description="Certification does not exist")
            return sawtooth_api.proto_to_dict(cert)

        data['certifications'] = [_get_cert(c) for c in data['certifications']]

        return Response(
            data=data
        )

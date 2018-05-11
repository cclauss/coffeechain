from base64 import b64decode

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from coffeechain.proto.coffee_pb2 import Certification, Roast, Harvest, Shipment, Farm
from coffeechain.services import sawtooth_api

pb_class_map = dict(
    cert=Certification,
    roast=Roast,
    harvest=Harvest,
    shipment=Shipment,
    farm=Farm,
)


class AddressView(APIView):

    def get(self, request, addr, as_type=None):
        data = sawtooth_api.client.state(addr)
        data['address'] = addr
        if as_type:
            bytes_data = b64decode(data['data'])
            try:
                cls = pb_class_map.get(as_type, None)
                if None:
                    raise ValidationError("Type '%s' is not known" % as_type)
                obj = cls()
                obj.ParseFromString(bytes_data)
                data['object'] = sawtooth_api.proto_to_dict(obj)
            except Exception as e:
                data['object'] = None
                data['object_decode_error'] = {
                    "message": "%s" % e,
                    "raw_data": repr(bytes_data).lstrip("b'").rstrip('').replace("\\", "\\")
                }

        return Response(data=data)

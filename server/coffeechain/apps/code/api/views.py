from rest_framework.response import Response
from rest_framework.views import APIView

from coffeechain.utils.drf.validation import validate_using
from . import serializers


class MintCodes(APIView):
    def post(self, request, *args):
        data = validate_using(serializers.MintCodesSerializer, data=request.data)
        return Response(
            data=data
        )

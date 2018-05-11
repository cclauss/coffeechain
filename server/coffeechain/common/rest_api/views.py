from rest_framework.response import Response
from rest_framework.views import APIView

from coffeechain.proto import address
from coffeechain.services import sawtooth_api


def block_data_view(pb_class):
    """
    Generates a view which returns blockchain data for a key
    - requires url kwarg called *key*
    """

    class _BlockChainDataView(APIView):
        def get(self, request, key=None):
            addr = address.addr_map[pb_class](key)
            roast = sawtooth_api.get_or_404(pb_class, addr)
            state_data = sawtooth_api.client.state(addr)
            return Response(data={
                "address": addr,
                "state": state_data,
                "head_block": sawtooth_api.client.block(state_data['head']),
                "object": sawtooth_api.proto_to_dict(roast)
            })

    return _BlockChainDataView.as_view()

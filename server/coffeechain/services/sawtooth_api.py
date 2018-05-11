import hashlib
import string
from base64 import b64decode

import requests
from django.conf import settings
from google.protobuf.json_format import MessageToDict
from requests import Response
from rest_framework.exceptions import NotFound
from rest_framework.utils import json
from sawtooth_sdk.protobuf.batch_pb2 import BatchHeader, Batch, BatchList
from sawtooth_sdk.protobuf.transaction_pb2 import TransactionHeader, Transaction

from coffeechain.proto import address, coffee_pb2, config
from coffeechain.proto.coffee_pb2 import CoffeeChainEvents
from coffeechain.utils.misc import as_list

_signer = settings.SAWTOOTH_SIGNER


def _post(url: str, data: dict) -> Response:
    return requests.post(
        url=settings.SAWTOOTH_API + url,
        data=data,
        headers={
            'Content-Type': 'application/octet-stream'
        }
    )


def proto_to_dict(obj):
    return MessageToDict(
        obj,
        including_default_value_fields=True,
        preserving_proto_field_name=True,
    )


class SawtoothNotFoundException(NotFound):
    """
    Dervies from rest_framework.NotFound so that it will automatically raise
    an http 404 if the call to sawtooth fails
    """

    def __init__(self, message="", url="", data=None):
        self.url = url
        self.json = data or {}
        super().__init__(detail=data)


class SawtoothClient(object):
    def _get(self, url, timeout=2) -> dict:
        print("calling: %s" % url)
        try:
            resp = requests.get(settings.SAWTOOTH_API + url, timeout=2)
            if resp.status_code == 404:
                raise SawtoothNotFoundException(url=url, data=resp.json())
            return resp.json()
        except SawtoothNotFoundException:
            raise
        except Exception:
            raise Exception("Sawtooth Call Failed")

    def state(self, addr, timeout: int = 2):
        assert len(addr) == 70, "Asset key must be 70 hex chars"
        assert all(k in string.hexdigits for k in addr), "Asset key must be 100% hex digits"
        data = self._get("/state/%s" % addr, timeout)
        data.pop('link')
        return data

    def block(self, block_id: str, timeout: int = 2) -> dict:
        assert len(block_id) == 128, "Address must be 70 hex chars"
        assert all(k in string.hexdigits for k in block_id), "Asset key must be 100% hex digits"
        data = self._get("/blocks/%s" % block_id, timeout)
        data.pop('link', None)
        return data.get('data', data)


client = SawtoothClient()


def get_state(addr: str) -> (any, str):
    assert len(addr) == 70, "Asset key must be 70 hex chars"
    assert all(k in string.hexdigits for k in addr), "Asset key must be 100% hex digits"

    try:
        data = client.state(addr)
        return None, b64decode(data['data'])
    except SawtoothNotFoundException as e:
        return 404, e.json


def parse_state_as(protobuf_class, data):
    """
    Parses the state['data'] field from swawtooth:8008/state/{address} as the
    specified type of protobuf object and returns it.
    """
    obj = protobuf_class()
    obj.ParseFromString(data)
    return obj


def get_state_as(protobuf_class, addr: str) -> (any, object):
    """
    Gets the state from sawtooth for the address, and parses it as a protobuf object
    :param protobuf_class: The class to convert to
    :param addr: The address (70 hex) to lookup
    :return (Error Code, Protobuf Object) -> If error, object will be null
    """
    err, data = get_state(addr)
    if not err:
        return None, parse_state_as(protobuf_class, data)
    else:
        return err, None


def state_exists(addr):
    """
    Returns true if the state address exists in sawtooth
    """
    try:
        client.state(addr)
        return True
    except SawtoothNotFoundException:
        return False
    except Exception:
        raise


def create_header(obj, outputs: [] = None, inputs: [] = None):
    return TransactionHeader(
        family_name=config.TXF_NAME,
        family_version=config.TXF_VERSION,
        inputs=inputs or [],
        outputs=outputs or [],
        signer_public_key=_signer.get_public_key().as_hex(),
        batcher_public_key=_signer.get_public_key().as_hex(),
        dependencies=[],
        payload_sha512=hashlib.sha512(obj.SerializeToString()).hexdigest()
    ).SerializeToString()


def create_txn(obj, outputs: [] = None, inputs: [] = None):
    """
    Creates both the transaction and header.  You must calculate the input/output addresses
    needed to run the transaction before calling, though (for now)
    """
    header = create_header(obj, outputs=outputs, inputs=inputs)
    return Transaction(
        header=header,
        header_signature=_signer.sign(header),
        payload=obj.SerializeToString()
    )


def event_transaction(name, cls, inputs=None, outputs=None, **kwargs):
    return create_txn(
        obj=CoffeeChainEvents(**{name: cls(**kwargs)}),
        inputs=inputs or [],
        outputs=outputs or []
    )


def submit_batch(transactions: []) -> dict:
    """
    Submits a batch, returning the JSON return value from the Sawtooth API
    :param transactions:
    :return:
    """

    transactions = as_list(transactions)

    batch_header_bytes = BatchHeader(
        signer_public_key=_signer.get_public_key().as_hex(),
        transaction_ids=[t.header_signature for t in transactions],
    ).SerializeToString()

    signature = _signer.sign(batch_header_bytes)
    batch = Batch(
        header=batch_header_bytes,
        header_signature=signature,
        transactions=transactions
    )

    batch_list_bytes = BatchList(batches=[batch]).SerializeToString()
    resp = _post("/batches", batch_list_bytes)
    resp_data = resp.json()
    print(json.dumps(resp_data, indent=4))

    return resp_data


def submit_event(inputs=None, outputs=None, **kwargs):
    """
    This is the primary way to submit data to sawtooth.  Most other
    methods are just helpers.
    todo: write a better description
    """
    assert len(kwargs) == 1, "Only one event type can be sent (e.g. harvest_create)"
    return submit_batch(
        create_txn(
            obj=CoffeeChainEvents(**kwargs),
            inputs=inputs or [],
            outputs=outputs or []
        )
    )


def get_or_404(pb_class, addr: str):
    err, obj = get_state_as(pb_class, addr)
    if err:
        raise NotFound(
            detail={
                "error": "Error retrieving %s" % pb_class.__name__,
                "error_code": err,
                "details": {
                    "address": addr
                }
            }
        )
    return obj


def get_raw_state_or_404(addr: str) -> dict:
    """
    Same as get_or_404, but returns the raw data at the address
    """
    err, obj = get_raw_state(addr)
    if err:
        raise NotFound(
            detail={
                "error": "Error retrieving %s" % addr,
                "error_code": err,
                "details": {
                    "address": addr
                }
            }
        )
    return obj


def resolve_keys(item, list_key, pb_class, key_field="key"):
    initial_data = item[list_key]
    resolved_data = []

    for key in initial_data:
        addr = address.addr_map[pb_class](key)
        err, cert = get_state_as(pb_class, addr)
        if err:
            cert = pb_class(key=key, description="%s not found" % pb_class.__name__)
        resolved_data.append(proto_to_dict(cert))

    item[list_key] = resolved_data

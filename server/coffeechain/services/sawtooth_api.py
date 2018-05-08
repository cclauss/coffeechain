import hashlib
import string
from base64 import b64decode

import requests
from django.conf import settings
from google.protobuf.json_format import MessageToDict
from requests import Response
from rest_framework.utils import json
from sawtooth_sdk.protobuf.batch_pb2 import BatchHeader, Batch, BatchList
from sawtooth_sdk.protobuf.transaction_pb2 import TransactionHeader, Transaction

from coffeechain.proto import address, coffee_pb2, config
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


def get_state(addr: str) -> (any, str):
    assert len(addr) == 70, "Asset key must be 70 hex chars"
    assert all(k in string.hexdigits for k in addr), "Asset key must be 100% hex digits"

    url = settings.SAWTOOTH_API + "/state/%s" % addr
    print("calling: %s" % url)
    resp = requests.get(url, timeout=2)

    if resp.status_code == 404:
        print("Got 404")
        return 404, resp.json()
    else:
        print("Got asset")
        data = resp.json()
        print(json.dumps(data, indent=4))
        return None, b64decode(data['data'])


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
        return None, parse_state_as(coffee_pb2.Code, data)
    else:
        return err, None


def get_code(message: str) -> coffee_pb2.Code:
    err, data = get_state(address.for_code(message))
    if not err:
        return parse_state_as(coffee_pb2.Code, data)
    else:
        return None


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

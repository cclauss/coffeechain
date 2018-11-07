from sha3 import sha3_256

from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

from coffeechain.common.constants import Chain
from coffeechain.utils.misc import get_timestamp

from django.conf import settings


def generate_bdb_keypair(passphrase: str):
    return generate_keypair(sha3_256(passphrase.encode()).digest())


if settings.CHAIN == Chain.BIGCHAIN:
    _bdb = BigchainDB(settings.BIGCHAINDB_API)
    _default_keypair = generate_bdb_keypair('DefaultUserKeys')


def create(
    data,
    metadata=None,
    issuer_keypair=None,
    recipient_pub_key=None,
    mode=None
):
    issuer_keypair = issuer_keypair or _default_keypair
    recipient_pub_key = recipient_pub_key or _default_keypair.public_key

    metadata = metadata or {'timestamp': get_timestamp()}
    tx = _bdb.transactions.prepare(
        operation='CREATE',
        signers=issuer_keypair.public_key,
        asset={'data': data},
        metadata=metadata,
        recipients=recipient_pub_key
    )
    return sign_and_send(tx, issuer_keypair, mode)


def transfer(
    asset_input_tx,
    metadata=None,
    owner_keypair=None,
    recipient_pub_key=None,
    mode=None
):
    metadata = metadata or {'timestamp': get_timestamp()}
    owner_keypair = owner_keypair or _default_keypair
    recipient_pub_key = recipient_pub_key or _default_keypair.public_key

    output = asset_input_tx['outputs'][0]
    inputs_ = {
        'fulfillment': output['condition']['details'],
        'fulfills': {
            'output_index': 0,
            'transaction_id': asset_input_tx['id'],
        },
        'owners_before': output['public_keys']
    }
    tx = _bdb.transactions.prepare(
        operation='TRANSFER',
        inputs=inputs_,
        asset={'id': get_transaction_id(asset_input_tx)},
        metadata=metadata,
        recipients=recipient_pub_key
    )
    return sign_and_send(tx, owner_keypair, mode)


def get_assets_by_user(public_key, spent=False):
    return _bdb.outputs.get(public_key, spent)


def get_asset(asset_id, operation=None):
    return _bdb.transactions.get(asset_id=asset_id, operation=operation)


def search_asset(query):
    return _bdb.assets.get(search=query)


def send_commit(signed_tx):
    return _bdb.transactions.send_commit(signed_tx)


def send_sync(signed_tx):
    return _bdb.transactions.send_sync(signed_tx)


def send_async(signed_tx):
    return _bdb.transactions.send_async(signed_tx)


def sign_and_send(tx, signer, mode=None):
    signed_tx = _bdb.transactions.fulfill(tx, signer.private_key)
    if mode == 'sync':
        return send_sync(signed_tx)
    elif mode == 'async':
        return send_async(signed_tx)

    return send_commit(signed_tx)


def get_transaction_id(transaction):
    return transaction['id'] if transaction['operation'] == 'CREATE' else transaction['asset']['id']


def fetch_transaction(tx_id):
    return _bdb.transactions.retrieve(tx_id)


def get_last_tx(query):
    query_result = search_asset(query)[0]['id']
    assert len(query_result) == 1, "Invalid number of records returned for provided search query"
    tx_list = get_asset(query_result)
    return tx_list[len(tx_list) - 1]


# Application specific methods

def find_one(query):
    result = search_asset(query)
    result_len = len(result)
    if result_len == 1:
        return None, result[0]['data']
    elif result_len == 0:
        return None, {}
    else:
        return "Error with certification data fetched. Got too many results.", None


def check_asset_exits(query):
    _, result = find_one(query)
    return False if result == {} else True

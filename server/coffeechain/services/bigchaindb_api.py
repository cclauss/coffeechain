from bigchaindb_driver import BigchainDB
bdb_root_url = 'http://localhost:9984'
bdb = BigchainDB(bdb_root_url)

def create(data, metadata, issuer_keypair, recipient_pub_key):
    tx = bdb.transactions.prepare(
            operation='CREATE', 
            signers=issuer_keypair.public_key,
            asset={
                'data': data
            },
            metadata=metadata,
            recipients=recipient_pub_key)
    return sign_and_send(tx, issuer_keypair)

def transfer(asset_input_tx, metadata, owner_keypair, recipient_pub_key):
    output = asset_input_tx['outputs'][0]
    inputs_ = {
        'fulfillment': output['condition']['details'],
        'fulfills': {
        'output_index': 0,
        'transaction_id': asset_input_tx['id'],
            },
        'owners_before': output['public_keys']
    }
    tx = bdb.transactions.prepare(
        operation='TRANSFER',
        inputs=inputs_,
        asset={'id': asset_input_tx['id']},
        metadata=metadata,
        recipients=recipient_pub_key)
    return sign_and_send(tx, owner_keypair)

def get_assets_by_user(public_key, spent=False):
    return bdb.outputs.get(public_key, spent)

def get_asset(asset_id, operation=None):
    return bdb.transactions.get(asset_id=asset_id, operation=operation)

def sign_and_send(tx, signer):
    signed_tx = bdb.transactions.fulfill(tx, signer.private_key)
    return bdb.transactions.send_commit(signed_tx)

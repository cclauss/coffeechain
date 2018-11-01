from bigchaindb_driver import BigchainDB
bdb_root_url = 'http://localhost:9984'
bdb = BigchainDB(bdb_root_url)

def create(data, metadata, issuer, recipient):
    tx = bdb.transactions.prepare(
            operation='CREATE', 
            signers=issuer.public_key,
            asset=data,
            metadata=metadata,
            recipients=recipient)
    return sign_and_commit(tx, issuer)

def transfer(asset_input_tx, metadata, owner, recipient):
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
        recipients=recipient)
    return sign_and_commit(tx, owner)

def get_assets_by_user(public_key, spent=False):
    return bdb.outputs.get(public_key, spent)

def get_asset(asset_id, operation=None):
    return bdb.transactions.get(asset_id, operation)

def sign_and_commit(tx, signer):
    signed_tx = bdb.transactions.fulfill(tx, private_keys=signer.private_key)
    return bdb.transactions.send_commit(signed_tx)
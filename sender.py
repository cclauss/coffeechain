"""
Sample script for playing with sending events to the
TXP without running a full server.
"""
import json
import logging
import os
import random
import string
from hashlib import sha512
from time import sleep

import requests
from sawtooth_sdk.protobuf.batch_pb2 import BatchHeader, Batch, BatchList
from sawtooth_sdk.protobuf.transaction_pb2 import TransactionHeader, Transaction
from sawtooth_signing import create_context, CryptoFactory

from sawtooth.proto import config
from sawtooth.proto import address
from sawtooth.proto.coffee_pb2 import CoffeeChainEvents, Events, Certification

logging.basicConfig()

KEYFILE = "./signer.key.priv"


def create_keyfile(keyfile):
    if not os.path.isfile(keyfile):
        print("Creating Sawtooth Key:\n\t%s" % keyfile)
        context = create_context('secp256k1')
        with open(keyfile, "wt") as f:
            f.write(context.new_random_private_key().as_hex())


def get_signer(keyfile):
    create_keyfile(keyfile)
    with open(keyfile, "rb") as f:
        from sawtooth_signing.secp256k1 import Secp256k1PrivateKey
        return CryptoFactory(create_context('secp256k1')).new_signer(Secp256k1PrivateKey.from_hex(f.read()))


class CoffeeClient(object):
    _transactions = []

    def __init__(self):
        self.signer = get_signer("./signer.key.priv")

    def _create_header(self, pb, outputs: [], inputs: []):
        return TransactionHeader(
            family_name=config.TXF_NAME,
            family_version=config.TXF_VERSION,
            inputs=inputs or [],
            outputs=outputs or [],
            signer_public_key=self.signer.get_public_key().as_hex(),
            batcher_public_key=self.signer.get_public_key().as_hex(),
            dependencies=[],
            payload_sha512=sha512(pb.SerializeToString()).hexdigest()
        ).SerializeToString()

    def mint_code(self, message):
        event = CoffeeChainEvents(
            mint_code=Events.MintCode(message=message)
        )
        header = self._create_header(
            event,
            outputs=[address.make_address(event.mint_code)],
            inputs=[],
        )

        tx = Transaction(
            header=header,
            header_signature=self.signer.sign(header),
            payload=event.SerializeToString()
        )

        self._transactions.append(tx)

    def cert_create(self,key,name):
        event = CoffeeChainEvents(cert_create=Certification(key=key,name=name))
        header = self._create_header(
            event,
            outputs=[address.make_address(event.cert_create)],
            inputs=[],
        )

        tx = Transaction(
            header=header,
            header_signature=self.signer.sign(header),
            payload=event.SerializeToString()
        )

        self._transactions.append(tx)

    def submit(self):
        batch_header_bytes = BatchHeader(
            signer_public_key=self.signer.get_public_key().as_hex(),
            transaction_ids=[t.header_signature for t in self._transactions],
        ).SerializeToString()

        signature = self.signer.sign(batch_header_bytes)

        batch = Batch(
            header=batch_header_bytes,
            header_signature=signature,
            transactions=self._transactions
        )

        batch_list_bytes = BatchList(batches=[batch]).SerializeToString()
        resp = requests.post(
            url='http://localhost:8008/batches',
            data=batch_list_bytes,
            headers={
                'Content-Type': 'application/octet-stream'
            }
        )
        resp_data = resp.json()
        print(json.dumps(resp_data, indent=4))

        if 'link' in resp_data:
            self.poll_status(resp_data['link'])

    def poll_status(self, link):
        for _ in range(3):
            resp = requests.get(link)
            data = resp.json()
            print(json.dumps(data, indent=4))
            if data['data'][0]['status'] == "COMMITTED":
                exit()
            sleep(1)


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


if __name__ == '__main__':
    client = CoffeeClient()
    client.mint_code("message-xyzabc123youassholeserializethis")
    client.cert_create("key","azerty")
    client.submit()

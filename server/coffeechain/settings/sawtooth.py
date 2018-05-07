import os

from sawtooth_signing import CryptoFactory, create_context
from sawtooth_signing.secp256k1 import Secp256k1PrivateKey

from ._base import BASE_DIR

SAWTOOTH_KEY_FILE = os.path.join(BASE_DIR, "signer.priv")

if not os.path.isfile(SAWTOOTH_KEY_FILE):
    SAWTOOTH_HAS_KEY = False
else:
    with open(SAWTOOTH_KEY_FILE, "rb") as f:
        SAWTOOTH_ENABLED = False
        SAWTOOTH_CONTEXT = create_context('secp256k1')
        SAWTOOTH_PRIVATE_KEY = Secp256k1PrivateKey.from_hex(f.read())
        SAWTOOTH_SIGNER = CryptoFactory(SAWTOOTH_CONTEXT).new_signer(SAWTOOTH_PRIVATE_KEY)

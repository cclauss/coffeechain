from pathlib import Path

from sawtooth_signing import CryptoFactory, create_context
from sawtooth_signing.secp256k1 import Secp256k1PrivateKey

from coffeechain.common.constants import Chain
from ._base import env, APP_ROOT, CHAIN

SAWTOOTH_KEY_FILE = APP_ROOT("signer.priv")

if CHAIN == Chain.SAWTOOTH:
    if not Path(SAWTOOTH_KEY_FILE).exists():
        SAWTOOTH_HAS_KEY = False
        SAWTOOTH_SIGNER = None
        SAWTOOTH_ENABLED = False
    else:
        with open(SAWTOOTH_KEY_FILE, "rb") as f:
            SAWTOOTH_ENABLED = True
            SAWTOOTH_CONTEXT = create_context('secp256k1')
            SAWTOOTH_PRIVATE_KEY = Secp256k1PrivateKey.from_hex(f.read())
            SAWTOOTH_SIGNER = CryptoFactory(SAWTOOTH_CONTEXT).new_signer(SAWTOOTH_PRIVATE_KEY)

    SAWTOOTH_API = env.str("SAWTOOTH_API", "http://localhost:8008/").rstrip("/")  # should not have trailing slash

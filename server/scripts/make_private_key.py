import os

from django.conf import settings
from sawtooth_signing import create_context


def create_keyfile(keyfile):
    if os.path.isfile(keyfile):
        print("Sawtooth Key Already Exists:\n\t%s" % keyfile)
    else:
        print("Creating Sawtooth Key:\n\t%s" % keyfile)
        context = create_context('secp256k1')
        with open(keyfile, "wt") as f:
            f.write(context.new_random_private_key().as_hex())


def run(*args, **kwargs):
    create_keyfile(settings.SAWTOOTH_KEY_FILE)

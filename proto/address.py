import hashlib

from pb import *
from sawtooth import config


def _hash(value):
    return config.ADDRESS_PREFIX + hashlib.sha512(value.encode("utf-8")).hexdigest()[-64:]


def _make_code_address(message):
    return _hash(message)


def make_address(event):
    if isinstance(event, Events.MintCode):
        return _make_code_address(event.message)
    elif isinstance(event, Code):
        return _make_code_address(event.message)
    else:
        raise ValueError("event type %s was unknown" % type(event))

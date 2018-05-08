import hashlib

from pb import *
from sawtooth import config


def _hash(value):
    return config.ADDRESS_PREFIX + hashlib.sha512(value.encode("utf-8")).hexdigest()[-64:]


def make_address(event):
    if isinstance(event, Events.MintCode):
        return for_code(event.message)
    elif isinstance(event, Code):
        return for_code(event.message)
    else:
        raise ValueError("event type %s was unknown" % type(event))


def for_code(message):
    return _hash(message)

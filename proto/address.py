import hashlib

from . import coffee_pb2 as p
from . import config


def _hash(value):
    return config.ADDRESS_PREFIX + hashlib.sha512(value.encode("utf-8")).hexdigest()[-64:]


def make_address(event):
    if isinstance(event, p.Events.MintCode):
        return for_code(event.message)
    elif isinstance(event, p.Code):
        return for_code(event.message)
    elif isinstance(event, p.Certification):
        return for_cert(event.key)
    elif isinstance(event, p.Harvest):
        return for_harvest(event.key)
    elif isinstance(event, p.Farm):
        return for_farm(event.key)
    else:
        raise ValueError("event type %s was unknown" % type(event))


def for_code(message):
    return _hash(message)


def for_cert(key):
    return _hash(key)


def for_farm(key):
    return _hash(key)


def for_harvest(key):
    return _hash(key)
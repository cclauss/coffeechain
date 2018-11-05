import arrow
import collections

from django.utils import six

def is_seq(obj):
    """
    True of the object is a sequence (list or tuple) but not a string
    """
    return isinstance(obj, collections.Sequence) and not isinstance(obj, six.string_types)


def as_list(obj):
    """
    Forces an object to be a sequence if it is a single object
    """
    if not is_seq(obj):
        return [obj]
    else:
        return obj

def get_timestamp():
    return arrow.utcnow().timestamp
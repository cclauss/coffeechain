import os
import time
import datetime
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
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

def check_bigchaindb_enable():
    return True if(os.environ.get('BIGCHAINDB', 'False') == 'True') else False
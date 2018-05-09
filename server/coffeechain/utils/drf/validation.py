from rest_framework.exceptions import ValidationError

from coffeechain.proto import address
from coffeechain.services import sawtooth_api
from coffeechain.utils.drf.utils import get_view_serializer_context


def validate_using(serializer_class, data, view=None, **kwargs):
    """
    Simple helper method that runs the data through the serializer and returns the validated
    data.  Will raise an exception if validation fails.
    """
    context = get_view_serializer_context(view, **kwargs) if view else kwargs
    ser = serializer_class(data=data, context=context)
    ser.is_valid(raise_exception=True)
    return ser.validated_data


def sawtooth_address_exists(address_func):
    addr_gen = getattr(address, address_func, None)
    assert addr_gen is not None, "address module function '%s' not found" % address_func

    def _validate(value):
        print("checking : %s" % value)
        if not sawtooth_api.state_exists(addr_gen(value)):
            raise ValidationError("State for '%s' does not exist" % value)

    return _validate


def sawtooth_address_doesnt_exist(address_func):
    addr_gen = getattr(address, address_func, None)
    assert addr_gen is not None, "address module function '%s' not found" % address_func

    def _validate(value):
        if sawtooth_api.state_exists(addr_gen(value)):
            raise ValidationError("State for '%s' alrady exists" % value)

    return _validate

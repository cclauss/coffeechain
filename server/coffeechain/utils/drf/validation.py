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

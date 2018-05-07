def get_view_serializer_context(view, **additional_context):
    """
    Gets the standard view serializer context, same as GenericAPIView does.  This also
    allows us to add additional values to the serializer context by passing in more kwargs.
    :param view: APIView class
    :return:
    """
    ctx = {
        'request': view.request,
        'format': view.format_kwarg,
        'view': view
    }
    if additional_context:
        ctx.update(additional_context)

    return ctx



def get_request_value_body(request, key, default_value):
    """
    To get passed key value from request object
    """

    if key in request.data:
        return request.data[key]

    return default_value


def get_query_param_value(request, key, default_value):
    """
    To get passed key value from request object
    """
    print(request.GET.get)
    import pdb
    pdb.set_trace()
    if key in request.GET.get:
        return request.GET.get[key]

    return default_value


def is_user_has_permission(request, module_name):
    """
    To get user accessibility for passed module
    """
    return True
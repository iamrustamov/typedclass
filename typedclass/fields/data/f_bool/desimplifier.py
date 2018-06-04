from contracts import contract


@contract
def desimplifier_bool(value):
    """
    :type value: TypedClassAny
    :rtype: bool|TypedClassAny
    """
    if isinstance(value, str):
        if value in ('false', '0'):
            return False
        if value in ('true', '1'):
            return True

    return value

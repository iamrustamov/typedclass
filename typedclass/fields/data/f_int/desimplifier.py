from contracts import contract


@contract
def desimplifier_int(value):
    """
    :type value: TypedClassAny
    :rtype: int|TypedClassAny
    """
    if isinstance(value, str) and value.isnumeric():
        return int(value)

    return value

from contracts import contract

from typedclass.exceptions import TypedClassValidationError


@contract
def desimplifier_float(value):
    """
    :type value: TypedClassAny
    :rtype: float|TypedClassAny
    """
    if isinstance(value, (str, int)):
        try:
            return float(value)
        except ValueError:
            raise TypedClassValidationError('Not a Float')

    return value

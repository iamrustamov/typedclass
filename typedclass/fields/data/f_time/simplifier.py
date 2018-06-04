from contracts import contract
import datetime as dt

from typedclass.exceptions import TypedClassValidationError


@contract
def simplifier_time(value):
    """
    :type value: TypedClassAny
    :rtype: str
    """
    if isinstance(value, dt.time):
        return value.strftime('%H:%M:%S')

    raise TypedClassValidationError('Not a time')

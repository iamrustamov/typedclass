from contracts import contract
import datetime as dt

from typedclass.exceptions import TypedClassValidationError


@contract
def simplifier_datetime(value):
    """
    :type value: TypedClassAny
    :rtype: str
    """
    if isinstance(value, dt.datetime):
        return value.strftime('%Y-%m-%dT%H:%M:%S:%f')

    raise TypedClassValidationError('Not a datetime')

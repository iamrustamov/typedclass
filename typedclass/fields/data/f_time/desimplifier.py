from contracts import contract
import datetime as dt

from typedclass.exceptions import TypedClassValidationError


@contract
def desimplifier_time(value):
    """
    :type value: TypedClassAny
    :rtype: TypedClassTime|TypedClassAny
    """
    if isinstance(value, str):
        try:
            return dt.datetime.strptime(value, '%H:%M:%S').time()
        except ValueError:
            pass

        try:
            return dt.datetime.strptime(value, '%H:%M').time()
        except ValueError:
            raise TypedClassValidationError('Not a time')

    return value

import datetime as dt

from contracts import contract

from typedclass.exceptions import TypedClassValidationError


@contract
def desimplifier_date(value):
    """
    :type value: TypedClassAny
    :rtype: TypedClassDate|TypedClassAny
    """
    if isinstance(value, str):
        try:
            return dt.datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError:
            raise TypedClassValidationError('Not a date')

    return value

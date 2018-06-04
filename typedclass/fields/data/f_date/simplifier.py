import datetime as dt

from contracts import contract

from typedclass.exceptions import TypedClassValidationError


@contract
def simplifier_date(value):
    """
    :type value: TypedClassAny
    :rtype: str
    """
    if isinstance(value, dt.date):
        return value.strftime('%Y-%m-%d')

    raise TypedClassValidationError('Not a date')

from contracts import contract
import datetime as dt

from typedclass.exceptions import TypedClassValidationError


@contract
def validator_date(field, value):
    """
    :type field: TypedClassBaseDataField
    :type value: TypedClassAny
    :rtype: None
    """
    if isinstance(value, dt.date) and not isinstance(value, dt.datetime):
        return

    raise TypedClassValidationError('Not a date')

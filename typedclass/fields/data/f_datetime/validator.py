from contracts import contract
import datetime as dt

from typedclass.exceptions import TypedClassValidationError


@contract
def validator_datetime(field, value):
    """
    :type field: TypedClassBaseDataField
    :type value: TypedClassAny
    :rtype: None
    """
    if isinstance(value, dt.datetime):
        return

    raise TypedClassValidationError('Not a datetime')

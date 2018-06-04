from contracts import contract
import datetime as dt

from typedclass.exceptions import TypedClassValidationError


@contract
def validator_time(field, value):
    """
    :type field: TypedClassBaseDataField
    :type value: TypedClassAny
    :rtype: None
    """
    if isinstance(value, dt.time):
        return

    raise TypedClassValidationError('Not a time')

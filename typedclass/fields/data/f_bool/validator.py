from contracts import contract
from typedclass.exceptions import TypedClassValidationError


@contract
def validator_bool(field, value):
    """
    :type field: TypedClassBaseDataField
    :type value: TypedClassAny
    :rtype: None
    """
    if isinstance(value, bool):
        return

    raise TypedClassValidationError('Not a bool')

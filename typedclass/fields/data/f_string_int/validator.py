from contracts import contract

from typedclass.exceptions import TypedClassValidationError


@contract
def validator_string_int(field, value):
    """
    :type field: TypedClassBaseDataField
    :rtype: None
    """
    if isinstance(value, (str, int, )):
        return

    raise TypedClassValidationError('Not a string / int')

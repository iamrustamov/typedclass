from contracts import contract

from typedclass.exceptions import TypedClassValidationError


@contract
def validator_binary(field, value):
    """
    :type field: TypedClassBaseDataField
    :rtype: None
    """
    if not isinstance(value, bytes):
        raise TypedClassValidationError('Not a binary')

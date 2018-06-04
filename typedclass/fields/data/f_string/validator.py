from contracts import contract

from typedclass.exceptions import TypedClassValidationError


@contract
def validator_string(field, value):
    """
    :type field: TypedClassBaseDataField
    :rtype: None
    """
    if not isinstance(value, str):
        raise TypedClassValidationError('Not a string')

    if field.min_length and len(value) < field.min_length:
        raise TypedClassValidationError('String length < {}'.format(field.min_length))

    if field.max_length and len(value) > field.max_length:
        raise TypedClassValidationError('String length > {}'.format(field.max_length))

    if field.choices and value not in field.choices:
        raise TypedClassValidationError('value not found in choices')

from contracts import contract

from typedclass.exceptions import TypedClassValidationError


@contract
def validator_int(field, value):
    """
    :type field: TypedClassBaseDataField
    :rtype: None
    """
    if not isinstance(value, int):
        raise TypedClassValidationError('Not an int')

    if field.min_value is not None and value < field.min_value:
        raise TypedClassValidationError('Int value < {}'.format(field.min_value))

    if field.max_value is not None and value > field.max_value:
        raise TypedClassValidationError('Int value > {}'.format(field.max_value))

    if field.choices and value not in field.choices:
        raise TypedClassValidationError('value not found in choices')

from contracts import contract

from typedclass.exceptions import TypedClassValidationError


@contract
def validator_float(field, value):
    """
    :type field: TypedClassBaseDataField
    :rtype: None
    """
    if not isinstance(value, float):
        raise TypedClassValidationError('Not an float')

    if field.min_value is not None and value < field.min_value:
        raise TypedClassValidationError('Float value < {}'.format(field.min_value))

    if field.max_value is not None and value > field.max_value:
        raise TypedClassValidationError('Float value > {}'.format(field.max_value))

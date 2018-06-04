from contracts import contract
from decimal import Decimal

from typedclass.exceptions import TypedClassValidationError


@contract
def validator_decimal(field, value):
    """
    :type field: TypedClassBaseDataField
    :type value: TypedClassAny
    :rtype: None
    """
    if not isinstance(value, Decimal):
        raise TypedClassValidationError('Not a Decimal')

    if field.min_value is not None and value < field.min_value:
        raise TypedClassValidationError('Decimal value < {}'.format(field.min_value))

    if field.max_value is not None and value > field.max_value:
        raise TypedClassValidationError('Decimal value > {}'.format(field.max_value))

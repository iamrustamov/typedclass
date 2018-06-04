from contracts import contract
from decimal import Decimal, DecimalException

from typedclass.exceptions import TypedClassValidationError


@contract
def desimplifier_decimal(value):
    """
    :type value: TypedClassAny
    :rtype: TypedClassDecimal|TypedClassAny
    """
    if isinstance(value, (str, int)):
        try:
            return Decimal(value)
        except DecimalException:
            raise TypedClassValidationError('Not a Decimal')

    return value

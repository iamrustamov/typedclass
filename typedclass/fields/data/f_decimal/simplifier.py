from contracts import contract
from decimal import Decimal

from typedclass.exceptions import TypedClassValidationError


@contract
def simplifier_decimal(value):
    """
    :type value: TypedClassAny
    :rtype: str
    """
    if isinstance(value, Decimal):
        return str(value)

    raise TypedClassValidationError('Not a Decimal')

from decimal import Decimal

from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.data.f_decimal.simplifier import simplifier_decimal


def test_ok():
    result = simplifier_decimal(Decimal('0.1234567890'))
    assert result == '0.1234567890'


def test_not_decimal_error():
    error = None
    try:
        simplifier_decimal(123)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not a Decimal'

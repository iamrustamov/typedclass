from decimal import Decimal

from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.data.f_decimal.desimplifier import desimplifier_decimal


def test_simplified_str():
    result = desimplifier_decimal('0.1234567890')
    assert isinstance(result, Decimal)
    assert result == Decimal('0.1234567890')


def test_simplified_int():
    result = desimplifier_decimal(123)
    assert isinstance(result, Decimal)
    assert result == Decimal('123.00')


def test_not_simplified():
    result_ok = Decimal('0.1234567890')
    result = desimplifier_decimal(result_ok)
    assert isinstance(result, Decimal)
    assert result == result_ok


def test_not_decimal_error():
    error = None
    try:
        desimplifier_decimal('test')
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not a Decimal'

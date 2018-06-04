from decimal import Decimal

from typedclass import fields as f
from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.data.f_decimal.validator import validator_decimal


def test_not_decimal():
    f_decimal = f.Decimal()

    error = None
    try:
        validator_decimal(f_decimal, 1)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not a Decimal'


def test_min_incorrect():
    f_decimal = f.Decimal(min_value=Decimal('0.01'))

    error = None
    try:
        validator_decimal(f_decimal, Decimal('0.009'))
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Decimal value < 0.01'


def test_max_incorrect():
    f_decimal = f.Decimal(max_value=Decimal('0.01'))

    error = None
    try:
        validator_decimal(f_decimal, Decimal('0.0101'))
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Decimal value > 0.01'


def test_ok():
    f_decimal = f.Decimal(min_value=Decimal('0.01'), max_value=Decimal('0.01'))
    validator_decimal(f_decimal, Decimal('0.01'))

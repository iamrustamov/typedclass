import datetime as dt

from typedclass import fields as f
from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.data.f_date.validator import validator_date


def test_ok():
    f_date = f.Date()

    validator_date(f_date, dt.date.today())


def test_error_datetime():
    f_date = f.Date()

    error = None
    try:
        validator_date(f_date, dt.datetime.now())
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not a date'


def test_error_another_type():
    f_date = f.Date()

    error = None
    try:
        validator_date(f_date, 14)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not a date'

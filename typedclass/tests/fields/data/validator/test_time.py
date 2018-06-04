import datetime as dt

from typedclass import fields as f
from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.data.f_time.validator import validator_time


def test_ok():
    f_time = f.Time()

    validator_time(f_time, dt.time(23, 59, 55))


def test_error_time():
    f_time = f.Time()

    error = None
    try:
        validator_time(f_time, dt.datetime.now())
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not a time'


def test_error_another_type():
    f_time = f.Time()

    error = None
    try:
        validator_time(f_time, 14)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not a time'

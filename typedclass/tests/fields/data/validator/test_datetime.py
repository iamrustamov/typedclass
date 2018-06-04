import datetime as dt

from typedclass import fields as f
from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.data.f_datetime.validator import validator_datetime


def test_ok():
    f_datetime = f.DateTime()

    validator_datetime(f_datetime, dt.datetime.now())


def test_error():
    f_datetime = f.DateTime()

    error = None
    try:
        validator_datetime(f_datetime, 1)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not a datetime'

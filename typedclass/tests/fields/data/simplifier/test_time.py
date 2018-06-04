import datetime as dt

from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.data.f_time.simplifier import simplifier_time


def test_ok():
    result = simplifier_time(dt.time(23, 59, 55))
    assert result == '23:59:55'


def test_not_time_error():
    error = None
    try:
        simplifier_time(123)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not a time'

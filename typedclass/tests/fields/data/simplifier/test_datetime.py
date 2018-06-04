import datetime as dt

from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.data.f_datetime.simplifier import simplifier_datetime


def test_ok():
    result = simplifier_datetime(dt.datetime(2017, 4, 20, 18, 50, 13, 36574))
    assert result == '2017-04-20T18:50:13:036574'


def test_not_datetime_error():
    error = None
    try:
        simplifier_datetime(123)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not a datetime'

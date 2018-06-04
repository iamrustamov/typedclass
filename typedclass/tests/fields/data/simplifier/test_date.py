import datetime as dt

from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.data.f_date.simplifier import simplifier_date


def test_ok():
    result = simplifier_date(dt.date(2017, 4, 20))
    assert result == '2017-04-20'


def test_not_date_error():
    error = None
    try:
        simplifier_date(123)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not a date'

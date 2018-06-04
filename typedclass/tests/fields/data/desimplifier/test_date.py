import datetime as dt

from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.data.f_date.desimplifier import desimplifier_date


def test_simplified():
    result = desimplifier_date('2017-04-20')
    assert result == dt.date(2017, 4, 20)


def test_not_simplified():
    result_ok = dt.date(2017, 4, 20)
    result = desimplifier_date(result_ok)
    assert result == result_ok


def test_not_date_error():
    error = None
    try:
        desimplifier_date('2017-04-')
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not a date'

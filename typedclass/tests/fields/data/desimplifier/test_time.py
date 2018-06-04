import datetime as dt

from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.data.f_time.desimplifier import desimplifier_time


def test_simplified1():
    result = desimplifier_time('23:59:55')
    assert result == dt.time(23, 59, 55)


def test_simplified2():
    result = desimplifier_time('23:59')
    assert result == dt.time(23, 59)


def test_not_simplified():
    result_ok = dt.time(23, 59, 55)
    result = desimplifier_time(result_ok)
    assert result == result_ok


def test_not_time_error():
    error = None
    try:
        desimplifier_time('23:59:')
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not a time'

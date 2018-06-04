import datetime as dt

from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.data.f_datetime.desimplifier import desimplifier_datetime


def test_simplified1():
    result = desimplifier_datetime('2017-04-20T18:50:13:036574')
    assert result == dt.datetime(2017, 4, 20, 18, 50, 13, 36574)


def test_simplified2():
    result = desimplifier_datetime('2017-04-20T18:50:13Z')
    assert result == dt.datetime(2017, 4, 20, 18, 50, 13)


def test_simplified3():
    result = desimplifier_datetime('2017-04-20T18:00')
    assert result == dt.datetime(2017, 4, 20, 18, 00, 00)


def test_simplified4():
    result = desimplifier_datetime('2017-04-20T18:00:00')
    assert result == dt.datetime(2017, 4, 20, 18, 00, 00)


def test_not_simplified():
    result_ok = dt.datetime(2017, 4, 20, 18, 50, 13, 36574)
    result = desimplifier_datetime(result_ok)
    assert result == result_ok


def test_not_datetime_error():
    error = None
    try:
        desimplifier_datetime('2017-04-')
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not a datetime'

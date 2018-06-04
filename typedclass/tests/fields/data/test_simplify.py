import datetime as dt
from decimal import Decimal
from unittest.mock import Mock, call

from typedclass import fields as f


def test_bool():
    f_bool = f.Bool()
    v_bool = True

    v_bool_simplified = f_bool.simplify(value=v_bool)

    assert v_bool_simplified == v_bool


def test_datetime():
    f_datetime = f.DateTime()
    v_datetime = dt.datetime(2017, 4, 20, 18, 50, 13, 36574)
    v_datetime_simplified_ok = '2017-04-20T18:50:13:036574'

    m_simplifier = Mock(return_value=v_datetime_simplified_ok)

    f_datetime.simplifier = m_simplifier
    v_datetime_simplified = f_datetime.simplify(value=v_datetime)

    assert m_simplifier.call_args_list == [
        call(v_datetime),
    ]

    assert v_datetime_simplified == v_datetime_simplified_ok


def test_datetime_empty():
    f_datetime = f.DateTime(required=False)

    m_simplifier = Mock()

    f_datetime.simplifier = m_simplifier
    v_datetime_simplified = f_datetime.simplify(value=None)

    assert m_simplifier.called is False
    assert v_datetime_simplified is None


def test_date():
    f_date = f.Date()
    v_date = dt.datetime(2017, 4, 20)
    v_date_simplified_ok = '2017-04-20'

    m_simplifier = Mock(return_value=v_date_simplified_ok)

    f_date.simplifier = m_simplifier
    v_date_simplified = f_date.simplify(value=v_date)

    assert m_simplifier.call_args_list == [
        call(v_date),
    ]

    assert v_date_simplified == v_date_simplified_ok


def test_date_empty():
    f_date = f.Date(required=False)

    m_simplifier = Mock()

    f_date.simplifier = m_simplifier
    v_date_simplified = f_date.simplify(value=None)

    assert m_simplifier.called is False
    assert v_date_simplified is None


def test_decimal():
    f_decimal = f.Decimal()
    v_decimal = Decimal('0.1234567890')
    v_decimal_simplified_ok = '0.1234567890'

    m_simplifier = Mock(return_value=v_decimal_simplified_ok)

    f_decimal.simplifier = m_simplifier
    v_decimal_simplified = f_decimal.simplify(value=v_decimal)

    assert m_simplifier.call_args_list == [
        call(v_decimal),
    ]

    assert v_decimal_simplified == v_decimal_simplified_ok


def test_int():
    f_int = f.Int()
    v_int = 12345

    v_int_simplified = f_int.simplify(value=v_int)

    assert v_int_simplified == v_int


def test_string():
    f_string = f.String()
    v_string = 'abc'

    v_string_simplified = f_string.simplify(value=v_string)

    assert v_string_simplified == v_string


def test_binary():
    f_binary = f.Binary()
    v_binary = b'abc'

    v_binary_simplified = f_binary.simplify(value=v_binary)

    assert v_binary_simplified == v_binary


def test_time():
    f_time = f.Time()
    v_time = dt.time(23, 59, 55)
    v_time_simplified_ok = '23:59:55'

    m_simplifier = Mock(return_value=v_time_simplified_ok)

    f_time.simplifier = m_simplifier
    v_time_simplified = f_time.simplify(value=v_time)

    assert m_simplifier.call_args_list == [
        call(v_time),
    ]

    assert v_time_simplified == v_time_simplified_ok


def test_time_empty():
    f_time = f.Time(required=False)

    m_simplifier = Mock()

    f_time.simplifier = m_simplifier
    v_time_simplified = f_time.simplify(value=None)

    assert m_simplifier.called is False
    assert v_time_simplified is None

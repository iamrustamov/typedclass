import datetime as dt
from decimal import Decimal
from unittest.mock import Mock, call

from typedclass import fields as f
from typedclass.exceptions import TypedClassValidationError


def test_bool():
    # create our new class, because we'll change it behaviour
    class TestBool(f.Bool):
        pass

    # set our mocked validators
    m_validator = Mock()
    m_extra_validator1 = Mock()
    m_extra_validator2 = Mock()
    TestBool.validators = (m_validator, )

    # set our mocked desimplifier
    v_bool_desimplified = True
    m_desimplifier = Mock(return_value=v_bool_desimplified)
    TestBool.desimplifier = m_desimplifier

    f_bool = TestBool(extra_validators=(m_extra_validator1, m_extra_validator2))
    v_bool = '1'
    f_bool.process(name='f_bool', value=v_bool)

    assert m_desimplifier.call_args_list == [
        call(v_bool),
    ]

    assert m_validator.call_args_list == [
        call(f_bool, v_bool_desimplified),
    ]

    assert m_extra_validator1.call_args_list == [
        call(f_bool, v_bool_desimplified),
    ]

    assert m_extra_validator2.call_args_list == [
        call(f_bool, v_bool_desimplified),
    ]


def test_datetime():
    # create our new class, because we'll change it behaviour
    class TestDateTime(f.DateTime):
        pass

    # set our mocked validators
    m_validator = Mock()
    m_extra_validator1 = Mock()
    m_extra_validator2 = Mock()
    TestDateTime.validators = (m_validator, )

    # set our mocked desimplifier
    v_datetime_desimplified = dt.datetime(2017, 4, 20, 18, 50, 13, 36574)
    m_desimplifier = Mock(return_value=v_datetime_desimplified)
    TestDateTime.desimplifier = m_desimplifier

    f_datetime = TestDateTime(extra_validators=(m_extra_validator1, m_extra_validator2))
    v_datetime = '2017-04-20T18:50:13:036574'
    f_datetime.process(name='f_datetime', value=v_datetime)

    assert m_desimplifier.call_args_list == [
        call(v_datetime),
    ]

    assert m_validator.call_args_list == [
        call(f_datetime, v_datetime_desimplified),
    ]

    assert m_extra_validator1.call_args_list == [
        call(f_datetime, v_datetime_desimplified),
    ]

    assert m_extra_validator2.call_args_list == [
        call(f_datetime, v_datetime_desimplified),
    ]


def test_date():
    # create our new class, because we'll change it behaviour
    class TestDate(f.Date):
        pass

    # set our mocked validators
    m_validator = Mock()
    m_extra_validator1 = Mock()
    m_extra_validator2 = Mock()
    TestDate.validators = (m_validator, )

    # set our mocked desimplifier
    v_date_desimplified = dt.date(2017, 4, 20)
    m_desimplifier = Mock(return_value=v_date_desimplified)
    TestDate.desimplifier = m_desimplifier

    f_date = TestDate(extra_validators=(m_extra_validator1, m_extra_validator2))
    v_date = '2017-04-20'
    f_date.process(name='f_date', value=v_date)

    assert m_desimplifier.call_args_list == [
        call(v_date),
    ]

    assert m_validator.call_args_list == [
        call(f_date, v_date_desimplified),
    ]

    assert m_extra_validator1.call_args_list == [
        call(f_date, v_date_desimplified),
    ]

    assert m_extra_validator2.call_args_list == [
        call(f_date, v_date_desimplified),
    ]


def test_decimal():
    # create our new class, because we'll change it behaviour
    class TestDecimal(f.Decimal):
        pass

    # set our mocked validators
    m_validator = Mock()
    m_extra_validator1 = Mock()
    m_extra_validator2 = Mock()
    TestDecimal.validators = (m_validator, )

    # set our mocked desimplifier
    v_decimal_desimplified = Decimal('0.1234567890')
    m_desimplifier = Mock(return_value=v_decimal_desimplified)
    TestDecimal.desimplifier = m_desimplifier

    f_decimal = TestDecimal(extra_validators=(m_extra_validator1, m_extra_validator2))
    v_decimal = '0.1234567890'
    f_decimal.process(name='f_decimal', value=v_decimal)

    assert m_desimplifier.call_args_list == [
        call(v_decimal),
    ]

    assert m_validator.call_args_list == [
        call(f_decimal, v_decimal_desimplified),
    ]

    assert m_extra_validator1.call_args_list == [
        call(f_decimal, v_decimal_desimplified),
    ]

    assert m_extra_validator2.call_args_list == [
        call(f_decimal, v_decimal_desimplified),
    ]


def test_int():
    # create our new class, because we'll change it behaviour
    class TestInt(f.Int):
        pass

    # set our mocked validators
    m_validator = Mock()
    m_extra_validator1 = Mock()
    m_extra_validator2 = Mock()
    TestInt.validators = (m_validator, )

    # set our mocked desimplifier
    v_int_desimplified = 12345
    m_desimplifier = Mock(return_value=v_int_desimplified)
    TestInt.desimplifier = m_desimplifier

    f_int = TestInt(extra_validators=(m_extra_validator1, m_extra_validator2))
    v_int = '12345'
    f_int.process(name='f_int', value=v_int)

    assert m_desimplifier.call_args_list == [
        call(v_int),
    ]

    assert m_validator.call_args_list == [
        call(f_int, v_int_desimplified),
    ]

    assert m_extra_validator1.call_args_list == [
        call(f_int, v_int_desimplified),
    ]

    assert m_extra_validator2.call_args_list == [
        call(f_int, v_int_desimplified),
    ]


def test_string():
    # create our new class, because we'll change it behaviour
    class TestString(f.String):
        pass

    # set our mocked validators
    m_validator = Mock()
    m_extra_validator1 = Mock()
    m_extra_validator2 = Mock()
    TestString.validators = (m_validator, )

    f_string = TestString(extra_validators=(m_extra_validator1, m_extra_validator2))
    v_string = 'abc'
    f_string.process(name='f_string', value=v_string)

    assert m_validator.call_args_list == [
        call(f_string, v_string),
    ]

    assert m_extra_validator1.call_args_list == [
        call(f_string, v_string),
    ]

    assert m_extra_validator2.call_args_list == [
        call(f_string, v_string),
    ]


def test_binary():
    # create our new class, because we'll change it behaviour
    class TestBinary(f.Binary):
        pass

    # set our mocked validators
    m_validator = Mock()
    m_extra_validator1 = Mock()
    m_extra_validator2 = Mock()
    TestBinary.validators = (m_validator, )

    f_binary = TestBinary(extra_validators=(m_extra_validator1, m_extra_validator2))
    v_binary = b'abc'
    f_binary.process(name='f_binary', value=v_binary)

    assert m_validator.call_args_list == [
        call(f_binary, v_binary),
    ]

    assert m_extra_validator1.call_args_list == [
        call(f_binary, v_binary),
    ]

    assert m_extra_validator2.call_args_list == [
        call(f_binary, v_binary),
    ]


def test_desimplifier_error():
    # create our new class, because we'll change it behaviour
    class TestBool(f.Bool):
        pass

    m_desimplifier = Mock(side_effect=TypedClassValidationError('test'))
    TestBool.desimplifier = m_desimplifier
    f_bool = TestBool()
    v_bool = '1'

    error = None
    try:
        f_bool.process(name='f_bool', value=v_bool)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'f_bool: test'


def test_time():
    # create our new class, because we'll change it behaviour
    class TestTime(f.Time):
        pass

    # set our mocked validators
    m_validator = Mock()
    m_extra_validator1 = Mock()
    m_extra_validator2 = Mock()
    TestTime.validators = (m_validator, )

    # set our mocked desimplifier
    v_time_desimplified = dt.time(23, 59, 55)
    m_desimplifier = Mock(return_value=v_time_desimplified)
    TestTime.desimplifier = m_desimplifier

    f_time = TestTime(extra_validators=(m_extra_validator1, m_extra_validator2))
    v_time = '23:59:55'
    f_time.process(name='f_time', value=v_time)

    assert m_desimplifier.call_args_list == [
        call(v_time),
    ]

    assert m_validator.call_args_list == [
        call(f_time, v_time_desimplified),
    ]

    assert m_extra_validator1.call_args_list == [
        call(f_time, v_time_desimplified),
    ]

    assert m_extra_validator2.call_args_list == [
        call(f_time, v_time_desimplified),
    ]

from typedclass import fields as f
from typedclass.core import TypedClass
from typedclass.exceptions import TypedClassValidationError


class Data(TypedClass):
    f_string = f.String()
    f_bool_opt = f.Bool(required=False)


def test_to_string():
    data = Data(
        f_string='test1',
    )
    data_str = data.to_string()
    assert (
        data_str == '{"f_string":"test1","f_bool_opt":null}'
        or
        data_str == '{"f_bool_opt":null,"f_string":"test1"}'
    )


def test_from_string():
    data_str = '{"f_string":"test1","f_bool_opt":null}'
    data = Data.from_string(data_str)
    data_ok = Data(
        f_string='test1',
    )
    assert data == data_ok


def test_from_string_error():
    error = None

    try:
        Data.from_string('')
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'load data error'

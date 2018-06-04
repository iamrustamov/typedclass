from typedclass import fields as f
from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.data.f_string_int.validator import validator_string_int


def test_not_string_int():
    f_string_int = f.StringInt()

    error = None
    try:
        validator_string_int(f_string_int, 1.23)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not a string / int'


def test_ok():
    f_string_int = f.StringInt()

    validator_string_int(f_string_int, 'abc')
    validator_string_int(f_string_int, 123)

from typedclass import fields as f
from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.data.f_bool.validator import validator_bool


def test_ok():
    f_bool = f.Bool()

    validator_bool(f_bool, False)
    validator_bool(f_bool, True)


def test_error():
    f_bool = f.Bool()

    error = None
    try:
        validator_bool(f_bool, 1)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not a bool'

from typedclass import fields as f
from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.data.f_binary.validator import validator_binary


def test_not_binary():
    f_binary = f.Binary()

    error = None
    try:
        validator_binary(f_binary, 1)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not a binary'

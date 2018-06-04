from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.data.f_float.desimplifier import desimplifier_float


def test_simplified():
    result = desimplifier_float('123.456')
    assert result == 123.456


def test_not_simplified():
    result_ok = 123.456
    result = desimplifier_float(result_ok)
    assert result == result_ok


def test_not_float_error():
    error = None
    try:
        desimplifier_float('test')
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not a Float'

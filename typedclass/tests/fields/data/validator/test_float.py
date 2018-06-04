from typedclass import fields as f
from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.data.f_float.validator import validator_float


def test_not_float():
    f_float = f.Float()

    error = None
    try:
        validator_float(f_float, '1')
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not an float'


def test_min_incorrect():
    f_float = f.Float(min_value=1.0)

    error = None
    try:
        validator_float(f_float, 0.0)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Float value < 1.0'


def test_max_incorrect():
    f_float = f.Float(max_value=1.0)

    error = None
    try:
        validator_float(f_float, 2.0)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Float value > 1.0'


def test_ok():
    f_float = f.Float(min_value=1.0, max_value=1.0)
    validator_float(f_float, 1.0)

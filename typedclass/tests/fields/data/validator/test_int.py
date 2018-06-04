from typedclass import fields as f
from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.data.f_int.validator import validator_int


def test_not_int():
    f_int = f.Int()

    error = None
    try:
        validator_int(f_int, '1')
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not an int'


def test_min_incorrect():
    f_int = f.Int(min_value=1)

    error = None
    try:
        validator_int(f_int, 0)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Int value < 1'


def test_max_incorrect():
    f_int = f.Int(max_value=1)

    error = None
    try:
        validator_int(f_int, 2)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Int value > 1'


def test_ok():
    f_int = f.Int(min_value=1, max_value=1, choices=(1, 2, ))
    validator_int(f_int, 1)


def test_choices_incorrect():
    f_int = f.Int(choices=(1, 2, ))

    error = None
    try:
        validator_int(f_int, 3)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'value not found in choices'

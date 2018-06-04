from typedclass import fields as f
from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.data.f_string.validator import validator_string


def test_not_string():
    f_string = f.String()

    error = None
    try:
        validator_string(f_string, 1)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not a string'


def test_min_incorrect():
    f_string = f.String(min_length=1)

    error = None
    try:
        validator_string(f_string, '')
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'String length < 1'


def test_max_incorrect():
    f_string = f.String(max_length=1)

    error = None
    try:
        validator_string(f_string, 'ab')
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'String length > 1'


def test_choices_incorrect():
    f_string = f.String(choices=('a', 'b'))

    error = None
    try:
        validator_string(f_string, 'c')
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'value not found in choices'


def test_ok_list():
    f_string = f.String(min_length=1, max_length=1, choices=['a', 'b'])
    validator_string(f_string, 'a')


def test_ok_tuple():
    f_string = f.String(min_length=1, max_length=1, choices=('a', 'b'))
    validator_string(f_string, 'a')

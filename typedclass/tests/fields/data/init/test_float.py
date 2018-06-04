from typedclass.exceptions import TypedClassError
from typedclass.fields.data.f_float.core import Float


def test_min_value_incorrect():
    error = None

    try:
        Float(min_value='test')
    except TypedClassError as exc:
        error = exc

    msg = str(error)
    assert msg == 'Incorrect min_value'


def test_max_value_incorrect():
    error = None

    try:
        Float(max_value='test')
    except TypedClassError as exc:
        error = exc

    msg = str(error)
    assert msg == 'Incorrect max_value'

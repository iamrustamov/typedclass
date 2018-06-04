from typedclass.exceptions import TypedClassError
from typedclass.fields.data.f_int.core import Int


def test_min_value_incorrect():
    error = None

    try:
        Int(min_value='test')
    except TypedClassError as exc:
        error = exc

    msg = str(error)
    assert msg == 'Incorrect min_value'


def test_max_value_incorrect():
    error = None

    try:
        Int(max_value='test')
    except TypedClassError as exc:
        error = exc

    msg = str(error)
    assert msg == 'Incorrect max_value'


def test_choices_incorrect():
    error = None

    try:
        Int(choices='test')
    except TypedClassError as exc:
        error = exc

    msg = str(error)
    assert msg == 'Incorrect choices'

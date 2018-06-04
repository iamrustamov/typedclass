from typedclass.exceptions import TypedClassError
from typedclass.fields.data.f_string.core import String


def test_min_length_incorrect():
    error = None

    try:
        String(min_length='test')
    except TypedClassError as exc:
        error = exc

    msg = str(error)
    assert msg == 'Incorrect min_length'


def test_max_length_incorrect():
    error = None

    try:
        String(max_length='test')
    except TypedClassError as exc:
        error = exc

    msg = str(error)
    assert msg == 'Incorrect max_length'


def test_choices_incorrect():
    error = None

    try:
        String(choices='test')
    except TypedClassError as exc:
        error = exc

    msg = str(error)
    assert msg == 'Incorrect choices'

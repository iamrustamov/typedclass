from typedclass import fields as f
from typedclass.core import TypedClass
from typedclass.exceptions import TypedClassError, TypedClassValidationError


class Entry(TypedClass):
    test = f.String()


def test_empty_data():
    error = None

    try:
        Entry()
    except TypedClassValidationError as exc:
        error = exc

    assert error


def test_ok():
    entry = Entry(test='abc')
    assert entry.test == 'abc'


def test_side_effect():
    entry = Entry(test='abc')

    error = None
    try:
        entry.entry_string_not_empty = 'test'
    except TypedClassError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'TypedClass is immutable'

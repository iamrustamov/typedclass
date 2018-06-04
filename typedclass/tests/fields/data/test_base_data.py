from typedclass.exceptions import TypedClassError
from typedclass.fields.data.base import BaseDataField
from typedclass.fields.data.f_bool.core import Bool


def test_validators_are_empty():
    error = None
    try:
        BaseDataField()
    except TypedClassError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'validators are empty'


def test_validators_are_not_iterable():
    error = None
    BaseDataField.validators = 123
    try:
        BaseDataField()
    except TypedClassError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'validators are not iterable'


def test_extra_validators_are_not_iterable():
    error = None
    try:
        Bool(extra_validators=123)
    except TypedClassError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'extra_validators are not iterable'

from typedclass import fields as f
from typedclass.core import TypedClass


class Entry(TypedClass):
    test = f.String()


def test_equal():
    entry1 = Entry(test='abc')
    entry2 = Entry(test='abc')
    assert entry1 == entry2


def test_not_equal():
    entry1 = Entry(test='abc')
    entry2 = Entry(test='abcde')
    assert entry1 != entry2


def test_not_implemented():
    entry = Entry(test='abc')
    is_equal = entry == ''
    assert is_equal is False

    is_not_equal = entry != ''
    assert is_not_equal is True

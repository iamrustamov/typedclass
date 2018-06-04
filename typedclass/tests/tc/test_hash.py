from typedclass import fields as f
from typedclass.core import TypedClass


class Entry(TypedClass):
    name = f.Int()


def test_hash1():
    entry1 = Entry(name=1)
    entry2 = Entry(name=1)
    assert set([entry1, entry2]) == set([entry1])


def test_hash2():
    entry1 = Entry(name=1)
    entry2 = Entry(name=2)
    assert set([entry1, entry2]) == set([entry1, entry2])

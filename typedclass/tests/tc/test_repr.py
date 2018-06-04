from typedclass import fields as f
from typedclass.core import TypedClass


class Entry(TypedClass):
    name = f.String()
    age = f.Int()


def test_repr():
    entry = Entry(**{'name': 'name1', 'age': 1})
    assert (
        entry.__repr__() == 'Entry(**{"age":1,"name":"name1"})'
        or
        entry.__repr__() == 'Entry(**{"name":"name1","age":1})'
    )

from typedclass import fields as f
from typedclass.core import TypedClass


class Data(TypedClass):
    string1 = f.String()
    string2 = f.String()


def test():
    data = Data(
        string1='string1',
        string2='string2',
    )
    data2 = data.update(
        string1='string3',
        string2='string4',
        unknown_field='unknown field',
    )
    assert data.string1 == 'string1'
    assert data.string2 == 'string2'
    assert data2.string1 == 'string3'
    assert data2.string2 == 'string4'
    assert data != data2

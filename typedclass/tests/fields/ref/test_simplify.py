from typedclass import fields as f
from typedclass.core import TypedClass


class Entry(TypedClass):
    test = f.String()


def test_empty_ok():
    f_ref = f.Ref(Entry, required=False)
    v_ref = f_ref.simplify(value=None)

    assert v_ref is None


def test_cls_ok():
    f_ref = f.Ref(Entry)
    entry = Entry(test='abc')
    v_ref = f_ref.simplify(value=entry)

    assert v_ref == {'test': 'abc'}

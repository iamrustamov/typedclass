from decimal import Decimal

from typedclass import fields as f
from typedclass.core import TypedClass
from typedclass.exceptions import TypedClassError


class Entry(TypedClass):
    test = f.String()


def test_cls_ok():
    f_set = f.Set(Entry)
    entry1 = Entry(test='abc')
    entry2 = Entry(test='xyz')
    entry3 = Entry(test='abc')
    entry4 = Entry(test='xyz')
    v_set = f_set.simplify(value={entry1, entry2, entry3, entry4})

    assert len(v_set) == 2
    assert {'test': 'abc'} in v_set
    assert {'test': 'xyz'} in v_set


def test_data_ok():
    f_set = f.Set(f.Decimal)
    v_set_ok = (Decimal('0.12345'), Decimal('6.7890'), Decimal('0.12345'), Decimal('6.7890'))

    v_set = f_set.simplify(value=v_set_ok)

    assert len(v_set) == 2
    assert '0.12345' in v_set
    assert '6.7890' in v_set


def test_unsupported_instance_error():
    f_set = f.Set(Entry)

    error = None
    try:
        f_set.simplify(value=(123, ))
    except TypedClassError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Unsupported type'


def test_empty_ok():
    f_set = f.Set(f.String, required=False)
    v_set = f_set.simplify(value=None)

    assert v_set is None

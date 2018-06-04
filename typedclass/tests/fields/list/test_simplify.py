from decimal import Decimal

from typedclass import fields as f
from typedclass.core import TypedClass
from typedclass.exceptions import TypedClassError


class Entry(TypedClass):
    test = f.String()


def test_cls_ok():
    f_list = f.List(Entry)
    entry1 = Entry(test='abc')
    entry2 = Entry(test='xyz')
    v_list = f_list.simplify(value=(entry1, entry2))

    assert v_list == tuple(({'test': 'abc'}, {'test': 'xyz'}))


def test_data_ok():
    f_list = f.List(f.Decimal)
    v_list_ok = (Decimal('0.12345'), Decimal('6.7890'))

    v_list = f_list.simplify(value=v_list_ok)

    assert v_list == tuple(('0.12345', '6.7890'))


def test_unsupported_instance_error():
    f_list = f.List(Entry)

    error = None
    try:
        f_list.simplify(value=(123, ))
    except TypedClassError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Unsupported type'


def test_empty_ok():
    f_list = f.List(f.String, required=False)
    v_list = f_list.simplify(value=None)

    assert v_list is None

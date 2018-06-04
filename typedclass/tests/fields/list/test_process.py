from typedclass import fields as f
from typedclass.core import TypedClass
from typedclass.exceptions import TypedClassValidationError


class Entry(TypedClass):
    test = f.String()


def test_empty_ok():
    f_list = f.List(f.String, required=False)
    v_list = f_list.process(name='f_list', value=None)

    assert v_list is None


def test_cls_ok():
    f_list = f.List(Entry)
    entry1 = Entry(test='abc')
    entry2_dict = {'test': 'xyz'}
    entry2 = Entry(**entry2_dict)
    v_list = f_list.process(name='f_list', value=(entry1, entry2_dict))

    assert v_list == tuple((entry1, entry2))


def test_data_ok():
    f_list = f.List(f.Bool)
    v_list_ok = ('0', 'true')

    v_list = f_list.process(name='f_list', value=v_list_ok)

    assert v_list == tuple((False, True))


def test_unsupported_instance_error():
    f_list = f.List(Entry)

    error = None
    try:
        f_list.process(name='f_list', value=(123, ))
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == (
        "f_list: element with idx 0 is not instance "
        "of <class 'typedclass.tests.fields.list.test_process.Entry'>"
    )


def test_not_list_error():
    f_list = f.List(f.Bool)

    error = None
    try:
        f_list.process(name='f_list', value=123)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == (
        "f_list is not list or tuple "
        "of <class 'typedclass.fields.data.f_bool.core.Bool'>"
    )

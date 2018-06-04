from typedclass import fields as f
from typedclass.core import TypedClass
from typedclass.exceptions import TypedClassValidationError


class Entry(TypedClass):
    test = f.String()


def test_empty_ok():
    f_set = f.Set(f.String, required=False)
    v_set = f_set.process(name='f_set', value=None)

    assert v_set is None


def test_cls_ok():
    f_set = f.Set(Entry)
    entry1 = Entry(test='abc')
    entry2_dict = {'test': 'xyz'}
    entry2 = Entry(**entry2_dict)
    entry3 = Entry(test='abc')
    entry4_dict = {'test': 'xyz'}
    v_set = f_set.process(name='f_set', value=(entry1, entry2_dict, entry3, entry4_dict))

    assert v_set == {entry1, entry2}


def test_data_ok():
    f_set = f.Set(f.Bool)
    v_set_ok = {'0', 'true', '0', 'true', 'false'}

    v_set = f_set.process(name='f_set', value=v_set_ok)

    assert v_set == {False, True}


def test_unsupported_instance_error():
    f_set = f.Set(Entry)

    error = None
    try:
        f_set.process(name='f_set', value={123})
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == (
        "f_set: element \"123\" is not instance "
        "of <class 'typedclass.tests.fields.set.test_process.Entry'>"
    )


def test_not_set_error():
    f_set = f.Set(f.Bool)

    error = None
    try:
        f_set.process(name='f_set', value=123)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == (
        "f_set is not set / frozenset / list / tuple "
        "of <class 'typedclass.fields.data.f_bool.core.Bool'>"
    )

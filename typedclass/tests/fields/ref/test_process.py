from typedclass import fields as f
from typedclass.core import TypedClass
from typedclass.exceptions import TypedClassValidationError


class Entry(TypedClass):
    test = f.String()


def test_empty_ok():
    f_ref = f.Ref(Entry, required=False)
    v_ref = f_ref.process(name='f_ref', value=None)

    assert v_ref is None


def test_cls_ok():
    f_ref = f.Ref(Entry)
    entry = Entry(test='abc')
    v_ref = f_ref.process(name='f_ref', value=entry)

    assert v_ref == entry


def test_dict_ok():
    f_ref = f.Ref(Entry)
    entry_dict = {'test': 'abc'}
    entry = Entry(**entry_dict)
    v_ref = f_ref.process(name='f_ref', value=entry_dict)

    assert v_ref == entry


def test_unsupported_instance_error():
    f_ref = f.Ref(Entry)

    error = None
    try:
        f_ref.process(name='f_ref', value=123)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == (
        "f_ref is not instance of "
        "<class 'typedclass.tests.fields.ref.test_process.Entry'>"
    )

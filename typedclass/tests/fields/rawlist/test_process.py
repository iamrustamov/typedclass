from typedclass import fields as f
from typedclass.exceptions import TypedClassValidationError


def test_ok():
    f_rawlist = f.RawList()
    v_rawlist_ok = [{'a': 'aa', 'b': 123, 'c': []}, {'d': 'dd', 'e': 123, 'f': []}]

    v_rawlist = f_rawlist.process(name='f_rawlist', value=v_rawlist_ok)

    assert v_rawlist == v_rawlist_ok


def test_empty_ok():
    f_rawlist = f.RawList(required=False)
    v_rawlist_ok = None

    v_rawlist = f_rawlist.process(name='f_rawlist', value=v_rawlist_ok)

    assert v_rawlist == v_rawlist_ok


def test_error():
    f_rawlist = f.RawList()

    error = None
    try:
        f_rawlist.process(name='f_rawlist', value={'a': 'aa'})
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'f_rawlist is not Sequence type'

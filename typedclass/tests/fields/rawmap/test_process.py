from typedclass import fields as f
from typedclass.exceptions import TypedClassValidationError


def test_ok():
    f_rawmap = f.RawMap()
    v_rawmap_ok = {'a': 'aa', 'b': 123, 'c': []}

    v_rawmap = f_rawmap.process(name='f_rawmap', value=v_rawmap_ok)

    assert v_rawmap == v_rawmap_ok


def test_empty_ok():
    f_rawmap = f.RawMap(required=False)
    v_rawmap_ok = None

    v_rawmap = f_rawmap.process(name='f_rawmap', value=v_rawmap_ok)

    assert v_rawmap == v_rawmap_ok


def test_error():
    f_rawmap = f.RawMap()

    error = None
    try:
        f_rawmap.process(name='f_rawmap', value=[1, 2, 3])
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'f_rawmap is not Mapping type'

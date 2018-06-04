from typedclass import fields as f
from typedclass.exceptions import TypedClassValidationError


def test_ok():
    f_typedmap = f.TypedMap(f.String(), f.Bool())

    v_typedmap = f_typedmap.process(name='f_typedmap', value={'a': '0', 'b': True})

    assert v_typedmap == {'a': False, 'b': True}


def test_empty_ok():
    f_typedmap = f.TypedMap(f.String(), f.Bool(), required=False)
    v_raw_map_ok = None

    v_typedmap = f_typedmap.process(name='f_typedmap', value=v_raw_map_ok)

    assert v_typedmap == v_raw_map_ok


def test_error():
    f_typedmap = f.TypedMap(f.String(), f.Bool())

    error = None
    try:
        f_typedmap.process(name='f_typedmap', value=123)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'f_typedmap is not Mapping type'

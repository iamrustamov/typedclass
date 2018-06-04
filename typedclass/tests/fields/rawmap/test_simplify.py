from typedclass import fields as f


def test_ok():
    f_rawmap = f.RawMap()
    v_rawmap_ok = {'a': 'aa', 'b': 123, 'c': []}

    v_rawmap = f_rawmap.simplify(value=v_rawmap_ok)

    assert v_rawmap == v_rawmap_ok


def test_empty_ok():
    f_rawmap = f.RawMap(required=False)
    v_rawmap_ok = None

    v_rawmap = f_rawmap.simplify(value=v_rawmap_ok)

    assert v_rawmap == v_rawmap_ok

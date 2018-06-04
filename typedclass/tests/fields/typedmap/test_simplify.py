from typedclass import fields as f


def test_ok():
    f_typedmap = f.TypedMap(f.String(), f.Bool())
    v_typedmap_ok = {'a': False, 'b': True}

    v_typedmap = f_typedmap.simplify(value=v_typedmap_ok)

    assert v_typedmap == v_typedmap_ok

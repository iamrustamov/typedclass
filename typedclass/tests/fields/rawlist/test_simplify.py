from typedclass import fields as f


def test_ok():
    f_rawlist = f.RawList()
    v_rawlist_ok = [{'a': 'aa', 'b': 123, 'c': []}, {'d': 'dd', 'e': 123, 'f': []}]

    v_rawlist = f_rawlist.simplify(value=v_rawlist_ok)

    assert v_rawlist == v_rawlist_ok


def test_empty_ok():
    f_rawlist = f.RawList(required=False)
    v_rawlist_ok = None

    v_rawlist = f_rawlist.simplify(value=v_rawlist_ok)

    assert v_rawlist == v_rawlist_ok

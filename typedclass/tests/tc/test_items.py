from typedclass import fields as f
from typedclass.core import TypedClass


INT1 = 12345
INT2 = 67890


class Entry(TypedClass):
    entry_int = f.Int()


class Data(TypedClass):
    entry_ref1 = f.Ref(Entry)
    entry_ref2 = f.Ref(Entry)
    entry_list = f.List(Entry)
    int1 = f.Int()
    int2 = f.Int()
    int_list = f.List(f.Int)


def test_items():
    entry1 = Entry(
        entry_int=INT1,
    )
    entry2 = Entry(
        entry_int=INT2,
    )
    data = Data(
        entry_ref1=entry1,
        entry_ref2=entry2,
        entry_list=[entry1, entry2],
        int1=INT1,
        int2=INT2,
        int_list=[INT1, INT2],
    )
    items_dict = {}
    for key, value in data.items():
        items_dict[key] = value

    items_dict_ok = {
        'entry_ref1': entry1,
        'entry_ref2': entry2,
        'entry_list': (entry1, entry2),
        'int1': INT1,
        'int2': INT2,
        'int_list': (INT1, INT2),
    }
    assert items_dict == items_dict_ok

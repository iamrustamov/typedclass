from typedclass import fields as f
from typedclass.core import TypedClass


class ItemFull(TypedClass):
    a = f.String()
    b = f.String()


class EntryFull(TypedClass):
    f_string_internal = f.String()
    f_string_public = f.String()
    f_items = f.List(ItemFull)


class DataFull(TypedClass):
    f_bool = f.Bool()
    f_ref = f.Ref(EntryFull)


class ItemCleaned(TypedClass):
    a = f.String()


class EntryCleaned(TypedClass):
    f_string_public = f.String()
    f_items = f.List(ItemCleaned)


class DataCleaned(TypedClass):
    f_bool = f.Bool()
    f_ref = f.Ref(EntryCleaned)


def test():
    item_full = ItemFull(
        a='aaa',
        b='bbb',
    )
    entry_full = EntryFull(
        f_string_internal='string_internal',
        f_string_public='string_public',
        f_items=[item_full],
    )
    data_full = DataFull(
        f_bool=True,
        f_ref=entry_full,
    )
    data_cleaned = data_full.convert_to(DataCleaned)

    item_cleaned = ItemCleaned(
        a='aaa',
    )
    entry_cleaned = EntryCleaned(
        f_string_public='string_public',
        f_items=[item_cleaned],
    )
    data_cleaned_ok = DataCleaned(
        f_bool=True,
        f_ref=entry_cleaned,
    )
    assert data_cleaned == data_cleaned_ok

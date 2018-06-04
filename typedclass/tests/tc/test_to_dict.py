import datetime as dt
from decimal import Decimal

from typedclass import fields as f
from typedclass.core import TypedClass


class Entry(TypedClass):
    f_string = f.String()


class Data(TypedClass):
    f_bool1 = f.Bool()
    f_bool2 = f.Bool()
    f_bool3_opt = f.Bool(required=False)
    f_datetime1 = f.DateTime()
    f_datetime2 = f.DateTime()
    f_decimal1 = f.Decimal()
    f_decimal2 = f.Decimal()
    f_ref1 = f.Ref(Entry)
    f_ref2 = f.Ref(Entry)
    f_ref3_list = f.List(Entry)


def test_to_dict():
    entry1 = Entry(
        f_string='test_string1',
    )
    entry2 = Entry(
        f_string='test_string2',
    )
    data = Data(
        f_bool1=True,
        f_bool2='false',
        f_datetime1=dt.datetime(2000, 12, 22, 18, 17, 5, 153639),
        f_datetime2='2012-05-11T23:59:59:999999',
        f_decimal1=Decimal('1.23'),
        f_decimal2='4.56',
        f_ref1=entry1,
        f_ref2={'f_string': 'test_string2'},
        f_ref3_list=[entry1, entry2],
    )
    data_dict = data.to_dict()
    data_dict_ok = {
        'f_bool1': True,
        'f_bool2': False,
        'f_bool3_opt': None,
        'f_datetime1': dt.datetime(2000, 12, 22, 18, 17, 5, 153639),
        'f_datetime2': dt.datetime(2012, 5, 11, 23, 59, 59, 999999),
        'f_decimal1': Decimal('1.23'),
        'f_decimal2': Decimal('4.56'),
        'f_ref1': {'f_string': 'test_string1'},
        'f_ref2': {'f_string': 'test_string2'},
        'f_ref3_list': [{'f_string': 'test_string1'}, {'f_string': 'test_string2'}],
    }
    assert data_dict == data_dict_ok

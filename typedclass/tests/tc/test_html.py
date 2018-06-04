from decimal import Decimal

from typedclass import fields as f
from typedclass.core import TypedClass


class Entry3(TypedClass):
    f_string3 = f.String()


class Entry2(TypedClass):
    f_string2 = f.String()
    f_entry3_ref = f.List(Entry3)


class Entry1(TypedClass):
    f_string1 = f.String()
    f_entry2_ref = f.List(Entry2)


def _extra_validator(field, value):  # pragma: no cover
    pass


class Data(TypedClass):
    # base:
    f_bool1 = f.Bool(required=True)
    f_bool2 = f.Bool(required=False, comment='test f_bool2')
    f_bool3 = f.Bool(extra_validators=(_extra_validator, ))

    f_date1 = f.Date(required=True)
    f_date2 = f.Date(required=False, comment='test f_date2')

    f_datetime1 = f.DateTime(required=True)
    f_datetime2 = f.DateTime(required=False, comment='test f_datetime2')

    f_decimal1 = f.Decimal(required=True)
    f_decimal2 = f.Decimal(required=False, comment='test f_decimal2')
    f_decimal3 = f.Decimal(min_value=Decimal('0.0001'), max_value=Decimal('1.234567890'))

    f_int1 = f.Int(required=True)
    f_int2 = f.Int(required=False, comment='test f_int2')
    f_int3 = f.Int(min_value=-999, max_value=999)

    f_float1 = f.Float(required=True)
    f_float2 = f.Float(required=False, comment='test f_float2')
    f_float3 = f.Float(min_value=1.23, max_value=4.56)

    f_string1 = f.String(required=True)
    f_string2 = f.String(required=False, comment='test f_string2')
    f_string3 = f.String(min_length=1, max_length=50, choices=('a', 'b',))
    f_string4 = f.String(choices=())

    f_time1 = f.Time(required=True)
    f_time2 = f.Time(required=False, comment='test f_time2')

    # special:
    f_list1 = f.List(f.String, required=True)
    f_list2 = f.List(f.String, required=False, comment='test f_list2')
    f_list3 = f.List(Entry1)

    f_ref1 = f.Ref(Entry1, required=True)
    f_ref2 = f.Ref(Entry1, required=False, comment='test f_ref2')

    f_set1 = f.Set(f.String, required=True)
    f_set2 = f.Set(f.String, required=False, comment='test f_set2')
    f_set3 = f.Set(Entry1)

    # map-like:
    f_rawmap1 = f.RawMap(required=True)
    f_rawmap2 = f.RawMap(required=False, comment='test f_rawmap2')

    f_typedmap1 = f.TypedMap(key=f.String(), value=f.String(), required=True)
    f_typedmap2 = f.TypedMap(key=f.String(), value=f.String(), required=False, comment='test f_typedmap2')

    # list-like:
    f_rawlist1 = f.RawList(required=True)
    f_rawlist2 = f.RawList(required=False, comment='test f_rawlist2')


def test_all():
    Data.gen_html()


def test_all_only_div():
    Data.gen_html(only_div=True)

import datetime as dt
from decimal import Decimal
from unittest.mock import call, patch

from typedclass import fields as f
from typedclass.core import TypedClass


class Entry(TypedClass):
    f_string = f.String()


class Data(TypedClass):
    f_bool = f.Bool()
    f_datetime = f.DateTime()
    f_date = f.Date()
    f_decimal = f.Decimal()
    f_int = f.Int()
    f_float = f.Float()
    f_string = f.String()
    f_list = f.List(f.String)
    f_ref = f.Ref(Entry)
    f_typedmap = f.TypedMap(key=f.String(), value=f.String())
    f_rawmap = f.RawMap()
    f_rawlist = f.RawList()
    f_time = f.Time()


@patch('typedclass.fields.data.base.BaseDataField.process')
@patch('typedclass.fields.special.ref.Ref.process')
@patch('typedclass.fields.typedmap.core.TypedMap.process')
@patch('typedclass.fields.special.list.List.process')
@patch('typedclass.fields.rawmap.core.RawMap.process')
@patch('typedclass.fields.rawlist.core.RawList.process')
def test(
    m_rawlist_process,
    m_rawmap_process,
    m_list_process,
    m_typedmap_process,
    m_ref_process,
    m_basedatafield_process,
):
    v_string1 = 'abc'
    entry = Entry(f_string=v_string1)
    v_bool = True
    v_date = dt.date.today()
    v_datetime = dt.datetime.now()
    v_decimal = Decimal('123.45')
    v_int = 123
    v_float = 123.456
    v_string2 = 'xyz'
    v_list = ('a', 'b')
    v_typedmap = {'a': 'aa', 'b': 'bb'}
    v_rawmap = {'a': 'aa', 'b': 123, 'c': []}
    v_rawlist = [{'a': 'aa', 'b': 123, 'c': []}, {'d': 'dd', 'e': 123, 'f': []}]
    v_time = dt.datetime.now().time()
    Data(
        f_bool=v_bool,
        f_date=v_date,
        f_datetime=v_datetime,
        f_decimal=v_decimal,
        f_int=v_int,
        f_float=v_float,
        f_string=v_string2,
        f_list=v_list,
        f_ref=entry,
        f_typedmap=v_typedmap,
        f_rawmap=v_rawmap,
        f_rawlist=v_rawlist,
        f_time=v_time,
    )

    assert len(m_basedatafield_process.call_args_list) == 9
    assert call(name='f_string', value=v_string1) in m_basedatafield_process.call_args_list
    assert call(name='f_bool', value=v_bool) in m_basedatafield_process.call_args_list
    assert call(name='f_decimal', value=v_decimal) in m_basedatafield_process.call_args_list
    assert call(name='f_date', value=v_date) in m_basedatafield_process.call_args_list
    assert call(name='f_datetime', value=v_datetime) in m_basedatafield_process.call_args_list
    assert call(name='f_int', value=v_int) in m_basedatafield_process.call_args_list
    assert call(name='f_float', value=v_float) in m_basedatafield_process.call_args_list
    assert call(name='f_string', value=v_string2) in m_basedatafield_process.call_args_list
    assert call(name='f_time', value=v_time) in m_basedatafield_process.call_args_list

    assert m_ref_process.call_args_list == [
        call(name='f_ref', value=entry),
    ]
    assert m_typedmap_process.call_args_list == [
        call(name='f_typedmap', value=v_typedmap),
    ]
    assert m_list_process.call_args_list == [
        call(name='f_list', value=v_list),
    ]
    assert m_rawmap_process.call_args_list == [
        call(name='f_rawmap', value=v_rawmap),
    ]
    assert m_rawlist_process.call_args_list == [
        call(name='f_rawlist', value=v_rawlist),
    ]

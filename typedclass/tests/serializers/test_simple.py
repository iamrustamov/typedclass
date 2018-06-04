import datetime as dt
from decimal import Decimal

from typedclass import fields as f
from typedclass.core import TypedClass


class Entry(TypedClass):
    entry_int = f.Int()


class Data(TypedClass):
    int = f.Int()
    int_list = f.List(f.Int)

    float = f.Float()
    float_list = f.List(f.Float)

    decimal = f.Decimal()
    decimal_list = f.List(f.Decimal)

    dt = f.DateTime()
    dt_list = f.List(f.DateTime)

    date = f.Date()
    date_list = f.List(f.Date)

    time = f.Time()
    time_list = f.List(f.Time)

    entry_ref = f.Ref(Entry)
    entry_list = f.List(Entry)

    rawmap = f.RawMap()
    rawlist = f.RawList()


def test():
    entry1 = Entry(
        entry_int=1,
    )
    entry2 = Entry(
        entry_int=2,
    )
    # ATTENTION!
    # default SimpleSerializer can't correct dump / load tuples and int keys like in :
    # rawmap = {
    #     'aaa': 123,
    #     ('bbb', 'ccc'): 'test',
    #     'ddd': {
    #         123: 456,
    #     },
    # }
    rawmap = {
        'aaa': 123,
        'bbb': 'test',
        'ccc': {
            'ddd': 456,
        },
    }
    rawlist = [
        {
            'aaa': 123,
            'bbb': 'test',
            'ccc': {
                'ddd': 456,
            },
        },
        {
            'eee': 789,
            'fff': 'test2',
            'ggg': {
                'hhh': 987,
            },
        },
    ]
    dt1 = dt.datetime(2000, 12, 22, 18, 17, 5, 153639)
    dt2 = dt.datetime(2012, 5, 11, 23, 59, 59, 999999)
    date1 = dt.date(2000, 12, 22)
    date2 = dt.date(2012, 5, 11)
    time1 = dt.time(23, 59, 55)
    time2 = dt.time(22, 49, 45)
    data = Data(
        int=3,
        int_list=[4, 5],
        float=3.0,
        float_list=[4.0, 5.0],
        decimal=Decimal('0.01'),
        decimal_list=[Decimal('1.23'), Decimal('4.56')],
        date=date1,
        date_list=[date1, date2],
        time=time1,
        time_list=[time1, time2],
        dt=dt1,
        dt_list=[dt1, dt2],
        entry_ref=entry1,
        entry_list=[entry1, entry2],
        rawmap=rawmap,
        rawlist=rawlist,
    )
    dumped = data.dumps()
    data2 = Data.loads(dumped)
    assert data == data2

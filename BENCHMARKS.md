# Benchmarks of Typedclass

benchmarks were executed with the schema:

```
class DataEntry(TypedClass):
    string1 = f.String(min_length=1)
    string2 = f.String(min_length=1)
    string3 = f.String()
    string4 = f.String()
    string5_opt = f.String(required=False)
    int1 = f.Int()
    int2 = f.Int()
    decimal1 = f.Decimal()
    decimal2 = f.Decimal()
    bool1 = f.Bool()
    bool2 = f.Bool()
    dt1 = f.DateTime()
    dt2 = f.DateTime()


class Data(TypedClass):
    entry1 = f.Ref(DataEntry)
    entry2 = f.Ref(DataEntry)
    entries1 = f.List(DataEntry)
    entries2 = f.List(DataEntry)
```

and with data:

```
_data_string1 = 'string1'
_data_string2 = 'string2'
_data_string_empty = ''
_data_int1 = 12345
_data_int2 = 67890
_data_decimal1 = Decimal('12345.67')
_data_decimal2 = '67890.12'
_data_bool1 = True
_data_bool2 = False
_data_dt1 = dt.datetime(2000, 12, 22, 18, 17, 5, 153639)
_data_dt2 = '2010-12-22T18:17:05:153639'


_data = {
    'string1': _data_string1,
    'string2': _data_string2,
    'string3': _data_string_empty,
    'string4': _data_string_empty,
    'int1': _data_int1,
    'int2': _data_int2,
    'decimal1': _data_decimal1,
    'decimal2': _data_decimal2,
    'bool1': _data_bool1,
    'bool2': _data_bool2,
    'dt1': _data_dt1,
    'dt2': _data_dt2,
}

DATA = {
    'entry1': _data,
    'entry2': _data,
    'entries1': [_data, _data],
    'entries2': [_data, _data],
}
```

### results:

|    lib      | bench time (in seconds) |  memory consumption (in mb) |
|    :---:    |           ----:         |              ---:           |
| typedclass  |           5.99          |             25.05           |
| schematics  |          18.01          |            123.10           |
|  pydantic   |           3.31          |            102.71           |
|  trafaret   |          24.45          |             42.17           |

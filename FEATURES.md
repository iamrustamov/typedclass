# Features of Typedclass

## Internal Storage

Internal storage of TypedClass is namedtuple,
so instances of TypedClass is immutable

## Fields

#### data:

 - Binary
 - Bool
 - Date
 - DateTime
 - Decimal
 - Int
 - Float
 - String
 - Time

all data fields support ```extra_validators``` param where you can dynamically add new validators without implementing separate field classes

#### special:

 - List
 - Ref (reference to another schema)
 - Set

#### map-like:

 - RawMap
 - TypedMap

#### list-like:

 - RawList


## Methods

all examples below are described with this schema & data:

```
class Entry(TypedClass):
    name = f.String()
    age = f.Int()
    birth_date = f.Date()

entry = Entry(name='Arnold', age=55, birth_date='1963-11-29')
```


### .simplify()

serialize data to simplified 'json-compatible' dict.

for deserializing back to python data just init instance of TypedClass with raw dict data.

```
> entry.simplify()
{'name': 'Arnold', 'age': 55, 'birth_date': '1963-11-29'}
```

### .to_string()

serialize data to string format with purpose of 
exchanging it with other process or for storage in DB.

```
> entry.to_string()
'{"name":"Arnold","age":55,"birth_date":"1963-11-29"}'
```

### .from_string()

deserialize data from string to TypedClass instance.

```
> entry = Entry.from_string('{"name":"Arnold","age":55,"birth_date":"1963-11-29"}')
```

### .to_dict()

convert data to python dict

```
> entry.to_dict()
{'age': 55, 'birth_date': datetime.date(1963, 11, 29), 'name': 'Arnold'}
```

### .update()

gen new TypedClass instance with updated data

```
> entry2 = entry.update(name='Felix')
> entry2.to_dict()
{'age': 55, 'birth_date': datetime.date(1963, 11, 29), 'name': 'Felix'}
> entry.to_dict()
{'age': 55, 'birth_date': datetime.date(1963, 11, 29), 'name': 'Arnold'}
```

### .dumps()

dump data with serializer

by default is SimpleSerializer used for json-compatible format via ujson lib.

also you can use MsgpackSerializer for msgpack-compatible format.

```
> entry.dumps()
'{"name":"Arnold","age":55,"birth_date":"1963-11-29"}'

> entry.dumps(serializer=MsgpackSerializer)
b'\x83\xa4name\xa6Arnold\xa3age7\xaabirth_date\xaa1963-11-29'
```

### .loads()

load data with serializer from dumped format

by default SimpleSerializer used for json-compatible format via ujson lib.

also you can use MsgpackSerializer for msgpack-compatible format.

```
> entry = Entry.loads('{"name":"Arnold","age":55,"birth_date":"1963-11-29"}')
> entry.to_dict()
{'age': 55, 'birth_date': datetime.date(1963, 11, 29), 'name': 'Arnold'}

> entry = Entry.loads(b'\x83\xa4name\xa6Arnold\xa3age7\xaabirth_date\xaa1963-11-29', serializer=MsgpackSerializer)
> entry.to_dict()
{'age': 55, 'birth_date': datetime.date(1963, 11, 29), 'name': 'Arnold'}
```

### .items()

method for iterating over keys & values in data

### .convert_to()

if we want to convert an instance of TypedClass with one schema
to an instance of TypedClass with another schema

```

class EntryInternal(TypedClass):
    name = f.String()
    age = f.Int()
    birth_date = f.Date()

class EntryPublic(TypedClass):
    name = f.String()
    age = f.Int()

> entry_internal = EntryInternal(name='Arnold', age=55, birth_date='1963-11-29')
> entry_public = entry_internal.convert_to(EntryPublic)
> entry_public.to_dict()
{'age': 55, 'name': 'Arnold'}

```

### .gen_html()

generates html with schema description

### is_tc_equal

typedclasses comparison helper for unit tests

```
> entry1 = Entry(name='Arnold', age=55, birth_date='1963-11-29')
> entry2 = Entry(name='Arnold', age=55, birth_date='1963-11-28')
> is_tc_equal(entry1, entry2)

--- a
+++ b
{
 'age': 55,
-'birth_date': datetime.date(1963, 11, 29),
+'birth_date': datetime.date(1963, 11, 28),
 'name': 'Arnold',
}
```

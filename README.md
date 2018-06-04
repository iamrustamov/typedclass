# Typedclass

## Description
Typedclass is class for data storage with features of:
 - validation
 - serialization
 - deserialization
 - html schema generation
 - comparison for unit tests

## Getting Started

### Installation

```
git clone

python setup.py install
```

### Example of usage

```
from typedclass import fields as f
from typedclass.core import TypedClass


# define schemas
class ChildEntry(TypedClass):
    age2 = f.Int(min_value=1, max_value=99)


class Entry(TypedClass):
    name = f.String()
    age = f.Int()
    birth_date = f.Date()
    child_entry = f.Ref(ChildEntry, required=False)


# validate raw data with schemas & init instance of typedclass
entry = Entry(
    name='Arnold',
    age='55',
    birth_date='1963-11-29',
    child_entry={'age2': 20},
)

# now we have validated data in python format
print(entry.to_dict())
# {'name': 'Arnold', 'age': 55, 'birth_date': datetime.date(1963, 11, 29), 'child_entry': {'age2': 20}}

# or we can convert it to simplified version for json response
print(entry.simplify())
# {'name': 'Arnold', 'age': 55, 'birth_date': '1963-11-29', 'child_entry': {'age2': 20}}
```

For all features see the [FEATURES.md](FEATURES.md) file for details.

For benchmarks see  [BENCHMARKS.md](BENCHMARKS.md) file for details.

### Running the tests

```
make test
```


## Authors

Alex Karev - Initial work

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

from typedclass import fields as f
from typedclass.core import TypedClass
from typedclass.compare import is_tc_equal


class Entry(TypedClass):
    name = f.String()
    age = f.Int()


class MyData(TypedClass):
    entries = f.Set(Entry)
    entries2 = f.List(Entry)
    debug1 = f.String(required=False)
    debug2 = f.String(required=False)


def test_is_tc_equal_false():
    tc1 = MyData(
        entries=[
            {'name': 'name1', 'age': 1},  # equal with tc2.name1
            {'name': 'name2', 'age': 2},  # exists only in tc1
            {'name': 'name3', 'age': 3},  # not equal with tc2.name3, age 3 != 33
            # None for name4, exists only in tc2
        ],
        entries2=[
            {'name': 'name8', 'age': 8},  # equal with tc2.name8
            {'name': 'name9', 'age': 9},  # not equal with tc2.name9, age 9 != 99
        ],
        debug1='tc1 debug1',
    )

    tc2 = MyData(
        entries=[
            {'name': 'name1', 'age': 1},  # equal with tc1.name1
            # None for name2, exists only in tc1
            {'name': 'name3', 'age': 33},  # not equal with tc1.name3, age 3 != 33
            {'name': 'name4', 'age': 4},  # exists only in tc2
        ],
        entries2=[
            {'name': 'name8', 'age': 8},  # equal with tc2.name8
            {'name': 'name9', 'age': 99},  # not equal with tc1.name9, age 9 != 99
        ],
        debug2='tc2 debug2',
    )
    result = is_tc_equal(tc1, tc2)
    assert result is False


def test_is_tc_equal_true():
    tc1 = MyData(entries=[], entries2=[])
    tc2 = MyData(entries=[], entries2=[])
    result = is_tc_equal(tc1, tc2)
    assert result is True

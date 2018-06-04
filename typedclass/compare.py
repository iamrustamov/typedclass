from contracts import contract
from datadiff import diff

from typedclass.core import TypedClass


@contract
def _convert_to_dict(value):
    """
    :type value: TypedClassAny
    :rtype: TypedClassAny
    """
    if isinstance(value, (set, frozenset, tuple, list)):
        new_value = list()
        for vv in value:
            new_value.append(_convert_to_dict(vv))

    elif isinstance(value, TypedClass):
        new_value = dict(value.items())

    else:
        new_value = value

    return new_value


@contract
def is_tc_equal(tc1, tc2):
    """
    comparing instances of TypedClass with pretty diff debug
    useful for unit tests

    path - using for recursive path

    :type tc1: TypedClass
    :type tc2: TypedClass
    :rtype: bool
    """
    is_equal = tc1 == tc2

    if is_equal:
        return is_equal

    # try to build pretty diff only if not equal
    # we don't need to implement our diff lib for now
    # we can just convert all TypedClass instances to dicts and use datadiff

    tc1_dict = dict(tc1.items())
    tc2_dict = dict(tc2.items())

    for key, value in tc1_dict.items():
        tc1_dict[key] = _convert_to_dict(value)

    for key, value in tc2_dict.items():
        tc2_dict[key] = _convert_to_dict(value)

    print(diff(tc1_dict, tc2_dict))

    return is_equal

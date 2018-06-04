from typedclass.fields.data.base import BaseDataField
from typedclass.fields.data.f_string_int.validator import validator_string_int


class StringInt(BaseDataField):
    """
    allow strings OR ints

    workaround for inconsistent data

    ATTENTION!
    this field without min_length / max_length / choices / min_value / max_value features!
    """
    validators = (validator_string_int, )

from typedclass.fields.data.base import BaseDataField
from typedclass.fields.data.f_string_english.validator import validator_string_english


class StringEnglish(BaseDataField):
    """
    allow english chars only

    ATTENTION!
    this field without min_length / max_length / choices / min_value / max_value features!
    """
    validators = (validator_string_english, )

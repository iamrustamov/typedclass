from typedclass.fields.data.base import BaseDataField
from typedclass.fields.data.f_string_email.validator import validator_string_email


class StringEmail(BaseDataField):
    """
    allow email only

    ATTENTION!
    this field without min_length / max_length / choices / min_value / max_value features!
    """
    validators = (validator_string_email, )

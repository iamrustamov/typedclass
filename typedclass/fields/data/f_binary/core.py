from typedclass.fields.data.base import BaseDataField
from typedclass.fields.data.f_binary.validator import validator_binary


class Binary(BaseDataField):
    validators = (validator_binary, )

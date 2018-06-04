from typedclass.fields.data.base import BaseDataField
from typedclass.fields.data.f_bool.desimplifier import desimplifier_bool
from typedclass.fields.data.f_bool.validator import validator_bool


class Bool(BaseDataField):
    desimplifier = staticmethod(desimplifier_bool)
    validators = (validator_bool, )

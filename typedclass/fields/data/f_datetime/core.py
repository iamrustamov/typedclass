from typedclass.fields.data.base import BaseDataField
from typedclass.fields.data.f_datetime.desimplifier import desimplifier_datetime
from typedclass.fields.data.f_datetime.simplifier import simplifier_datetime
from typedclass.fields.data.f_datetime.validator import validator_datetime


class DateTime(BaseDataField):
    simplifier = staticmethod(simplifier_datetime)
    desimplifier = staticmethod(desimplifier_datetime)
    validators = (validator_datetime, )

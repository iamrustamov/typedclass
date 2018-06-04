from typedclass.fields.data.base import BaseDataField
from typedclass.fields.data.f_date.desimplifier import desimplifier_date
from typedclass.fields.data.f_date.simplifier import simplifier_date
from typedclass.fields.data.f_date.validator import validator_date


class Date(BaseDataField):
    simplifier = staticmethod(simplifier_date)
    desimplifier = staticmethod(desimplifier_date)
    validators = (validator_date, )

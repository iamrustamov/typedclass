from typedclass.fields.data.base import BaseDataField
from typedclass.fields.data.f_time.desimplifier import desimplifier_time
from typedclass.fields.data.f_time.simplifier import simplifier_time
from typedclass.fields.data.f_time.validator import validator_time


class Time(BaseDataField):
    simplifier = staticmethod(simplifier_time)
    desimplifier = staticmethod(desimplifier_time)
    validators = (validator_time, )

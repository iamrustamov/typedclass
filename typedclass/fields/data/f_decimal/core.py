from contracts import contract
from decimal import Decimal as pyDecimal

from typedclass.exceptions import TypedClassError
from typedclass.fields.data.base import BaseDataField
from typedclass.fields.data.f_decimal.simplifier import simplifier_decimal
from typedclass.fields.data.f_decimal.desimplifier import desimplifier_decimal
from typedclass.fields.data.f_decimal.validator import validator_decimal


class Decimal(BaseDataField):
    simplifier = staticmethod(simplifier_decimal)
    desimplifier = staticmethod(desimplifier_decimal)
    validators = (validator_decimal, )

    @contract
    def __init__(self, min_value=None, max_value=None, required=True, comment=None, extra_validators=None):
        """
        :type self: TypedClassBaseDataField
        :type min_value: TypedClassDecimal|None|TypedClassAny
        :type max_value: TypedClassDecimal|None|TypedClassAny
        :type required: bool
        :type comment: str|None
        :type extra_validators: seq(TypedClassFunc)|None
        :rtype: None
        """
        if min_value is not None and not isinstance(min_value, pyDecimal):
            raise TypedClassError('Incorrect min_value')

        if max_value is not None and not isinstance(max_value, pyDecimal):
            raise TypedClassError('Incorrect max_value')

        super().__init__(required=required, comment=comment, extra_validators=extra_validators)
        self.min_value = min_value
        self.max_value = max_value

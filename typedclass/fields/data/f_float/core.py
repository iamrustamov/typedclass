from contracts import contract

from typedclass.exceptions import TypedClassError
from typedclass.fields.data.base import BaseDataField
from typedclass.fields.data.f_float.desimplifier import desimplifier_float
from typedclass.fields.data.f_float.validator import validator_float


class Float(BaseDataField):
    desimplifier = staticmethod(desimplifier_float)
    validators = (validator_float, )

    @contract
    def __init__(self, min_value=None, max_value=None, required=True, comment=None, extra_validators=None):
        """
        :type self: TypedClassBaseDataField
        :type min_value: float|None|TypedClassAny
        :type max_value: float|None|TypedClassAny
        :type required: bool
        :type comment: str|None
        :type extra_validators: seq(TypedClassFunc)|None
        :rtype: None
        """
        if min_value is not None and not isinstance(min_value, float):
            raise TypedClassError('Incorrect min_value')

        if max_value is not None and not isinstance(max_value, float):
            raise TypedClassError('Incorrect max_value')

        super().__init__(required=required, comment=comment, extra_validators=extra_validators)
        self.min_value = min_value
        self.max_value = max_value

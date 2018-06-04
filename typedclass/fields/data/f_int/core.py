from contracts import contract

from typedclass.exceptions import TypedClassError
from typedclass.fields.data.base import BaseDataField
from typedclass.fields.data.f_int.desimplifier import desimplifier_int
from typedclass.fields.data.f_int.validator import validator_int


class Int(BaseDataField):
    desimplifier = staticmethod(desimplifier_int)
    validators = (validator_int, )

    @contract
    def __init__(
        self, min_value=None, max_value=None, required=True, comment=None, extra_validators=None,
        choices=None,
    ):
        """
        :type self: TypedClassBaseDataField
        :type min_value: int|None|TypedClassAny
        :type max_value: int|None|TypedClassAny
        :type required: bool
        :type comment: str|None
        :type extra_validators: seq(TypedClassFunc)|None
        :type choices: seq(int)|None|TypedClassAny
        :rtype: None
        """
        if min_value is not None and not isinstance(min_value, int):
            raise TypedClassError('Incorrect min_value')

        if max_value is not None and not isinstance(max_value, int):
            raise TypedClassError('Incorrect max_value')

        if choices is not None and not isinstance(choices, (list, tuple)):
            raise TypedClassError('Incorrect choices')

        super().__init__(required=required, comment=comment, extra_validators=extra_validators)
        self.min_value = min_value
        self.max_value = max_value
        self.choices = choices

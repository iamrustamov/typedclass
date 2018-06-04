from contracts import contract

from typedclass.exceptions import TypedClassError
from typedclass.fields.data.base import BaseDataField
from typedclass.fields.data.f_string.validator import validator_string


class String(BaseDataField):
    validators = (validator_string, )

    @contract
    def __init__(
        self, min_length=None, max_length=None, required=True, comment=None, extra_validators=None,
        choices=None,
    ):
        """
        :type self: TypedClassBaseDataField
        :type min_length: int|None|TypedClassAny
        :type max_length: int|None|TypedClassAny
        :type required: bool
        :type comment: str|None
        :type extra_validators: seq(TypedClassFunc)|None
        :type choices: seq(str)|None
        :rtype: None
        """
        if min_length is not None and not isinstance(min_length, int):
            raise TypedClassError('Incorrect min_length')

        if max_length is not None and not isinstance(max_length, int):
            raise TypedClassError('Incorrect max_length')

        if choices is not None and not isinstance(choices, (list, tuple)):
            raise TypedClassError('Incorrect choices')

        super().__init__(required=required, comment=comment, extra_validators=extra_validators)
        self.min_length = min_length
        self.max_length = max_length
        self.choices = choices

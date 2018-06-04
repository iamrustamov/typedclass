from collections import Iterable
from contracts import contract

from typedclass.exceptions import TypedClassError, TypedClassValidationError
from typedclass.fields.base import BaseField


class BaseDataField(BaseField):
    simplifier = None
    desimplifier = None
    validators = None

    @contract
    def __init__(self, required=True, comment=None, extra_validators=None):
        """
        :type self: TypedClassBaseField
        :type required: bool
        :type comment: str|None
        :type extra_validators: seq(TypedClassFunc)|TypedClassAny|None
        :rtype: None
        """
        super().__init__(required=required, comment=comment)

        if self.validators is None:
            raise TypedClassError('validators are empty')

        if not isinstance(self.validators, Iterable):
            raise TypedClassError('validators are not iterable')

        validators = list(self.validators)
        if extra_validators is not None:
            if not isinstance(extra_validators, Iterable):
                raise TypedClassError('extra_validators are not iterable')

            validators.extend(list(extra_validators))

        self.all_validators = validators

    @contract
    def process(self, name, value):
        """
        :type self: TypedClassBaseField
        :type name: str
        :type value: TypedClassAny
        :rtype: TypedClassAny
        """
        if self.required is False and value is None:
            return

        if self.desimplifier is not None:
            try:
                value = self.desimplifier(value)
            except TypedClassValidationError as exc:
                raise TypedClassValidationError(
                    '{name}: {error}'.format(
                        name=name,
                        error=str(exc),
                    )
                )

        for func in self.all_validators:
            try:
                func(self, value)
            except TypedClassValidationError as exc:
                raise TypedClassValidationError(
                    '{name}: {error}'.format(
                        name=name,
                        error=str(exc),
                    )
                )

        return value

    @contract
    def simplify(self, value):
        """
        :type self: TypedClassBaseField
        :type value: TypedClassAny
        :rtype: TypedClassAny
        """
        if self.simplifier is not None:
            if self.required is False and value is None:
                return

            return self.simplifier(value)

        return value

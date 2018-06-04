from collections import Sequence
from contracts import contract

from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.base import BaseField


class RawList(BaseField):
    """
    ATTENTION!

    usually we shouldn't use this field at all!
    but in some cases when we want store some dynamic external data without parsing it
    & if this format compatible with serializers (json, msgpack, etc),
    we can use it.
    """
    @contract
    def process(self, name, value):
        """
        :type self: TypedClassBaseField
        :type name: str
        :type value: TypedClassAny
        :rtype: seq|None
        """
        if self.required is False and value is None:
            return

        if not isinstance(value, Sequence):
            raise TypedClassValidationError(
                '{} is not Sequence type'.format(name)
            )

        return value

    @contract
    def simplify(self, value):
        """
        :type self: TypedClassBaseField
        :type value: seq|None
        :rtype: seq|None
        """
        return value

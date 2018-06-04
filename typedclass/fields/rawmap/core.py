from collections import Mapping
from contracts import contract

from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.base import BaseField


class RawMap(BaseField):
    """
    ATTENTION!

    usually we shouldn't use this field at all!
    but in some cases when we want store some dynamic external data without parsing it
    & if this format compatible with serializers (json, msgpack, etc),
    we can use it.

    if key is not 'string' - it can be altered via serializer!
    i.e.
    ujson.dumps({1: 'test'})
    -->
    '{"1":"test"}'
    """
    @contract
    def process(self, name, value):
        """
        :type self: TypedClassBaseField
        :type name: str
        :type value: TypedClassAny
        :rtype: dict|None
        """
        if self.required is False and value is None:
            return

        if not isinstance(value, Mapping):
            raise TypedClassValidationError(
                '{} is not Mapping type'.format(name)
            )

        return value

    @contract
    def simplify(self, value):
        """
        :type self: TypedClassBaseField
        :type value: dict|None
        :rtype: dict|None
        """
        return value

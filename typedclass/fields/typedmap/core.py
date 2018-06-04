from collections import Mapping
from contracts import contract

from typedclass import fields as f
from typedclass.exceptions import TypedClassError, TypedClassValidationError
from typedclass.fields.base import BaseField


class TypedMap(BaseField):
    @contract
    def __init__(self, key, value, required=True, comment=None):
        """
        :type self: TypedClassBaseField
        :type key: TypedClassBaseField
        :type value: TypedClassBaseField
        :type required: bool
        :type comment: str|None
        :rtype: None
        """
        super().__init__(required=required, comment=comment)

        if not isinstance(key, f.String):
            raise TypedClassError('key type "String" supported only')

        self.key = key
        self.value = value

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

        converted = {}
        for _key, _value in value.items():
            _key_converted = self.key.process('key', _key)
            _value_converted = self.value.process('value of {}'.format(_key), _value)
            converted[_key_converted] = _value_converted

        return converted

    @contract
    def simplify(self, value):
        """
        :type self: TypedClassBaseField
        :type value: dict
        :rtype: dict
        """
        return value

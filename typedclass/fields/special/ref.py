from contracts import contract

from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.special.base import BaseSpecialField


class Ref(BaseSpecialField):
    @contract
    def process(self, name, value):
        """
        :type self: TypedClassBaseField
        :type name: str
        :type value: TypedClassAny
        :rtype: TypedClass|None
        """
        if self.required is False and value is None:
            return

        if isinstance(value, self.cls):
            return value
        elif isinstance(value, dict):
            f_instance = self.cls(**value)
            return f_instance
        else:
            raise TypedClassValidationError(
                '{name} is not instance of {cls}'.format(
                    name=name,
                    cls=self.cls,
                )
            )

    @contract
    def simplify(self, value):
        """
        :type self: TypedClassBaseField
        :type value: TypedClass|None
        :rtype: TypedClassAny
        """
        if value is None and self.required is False:
            return

        return value.simplify()

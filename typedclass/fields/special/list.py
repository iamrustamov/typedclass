from contracts import contract

from typedclass.exceptions import TypedClassError, TypedClassValidationError
from typedclass.fields.data.base import BaseDataField
from typedclass.fields.special.base import BaseSpecialField


class List(BaseSpecialField):
    @contract
    def process(self, name, value):
        """
        :type self: TypedClassBaseField
        :type name: str
        :type value: TypedClassAny
        :rtype: tuple|None
        """
        from typedclass.core import TypedClass
        # <-- circular import

        if self.required is False and value is None:
            return

        if isinstance(value, (tuple, list)):
            converted_value = []
            for idx, entry in enumerate(value):
                try:
                    if isinstance(entry, self.cls):
                        converted_value.append(entry)
                    elif isinstance(entry, dict) and issubclass(self.cls, TypedClass):
                        f_instance = self.cls(**entry)
                        converted_value.append(f_instance)
                    elif issubclass(self.cls, BaseDataField):
                        f_instance = self.cls()
                        _converted = f_instance.process(
                            name='{name}[{idx}]'.format(
                                name=name,
                                idx=idx,
                            ),
                            value=entry,
                        )
                        converted_value.append(_converted)
                    else:
                        raise TypedClassValidationError()
                except TypedClassValidationError:
                    raise TypedClassValidationError(
                        '{name}: element with idx {idx} is not instance of {cls}'.format(
                            name=name,
                            idx=idx,
                            cls=self.cls,
                        )
                    )
            return tuple(converted_value)
        else:
            raise TypedClassValidationError(
                '{name} is not list or tuple of {cls}'.format(
                    name=name,
                    cls=self.cls,
                )
            )

    @contract
    def simplify(self, value):
        """
        :type self: TypedClassBaseField
        :type value: TypedClassAny
        :rtype: tuple|None
        """
        result = []

        if value is None:
            return

        for entry in value:
            if isinstance(entry, self.cls):
                result.append(entry.simplify())
            elif issubclass(self.cls, BaseDataField):
                f_instance = self.cls()
                simplified = f_instance.simplify(entry)
                result.append(simplified)
            else:
                raise TypedClassError('Unsupported type')

        return tuple(result)

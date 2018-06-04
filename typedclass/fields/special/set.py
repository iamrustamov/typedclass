from contracts import contract

from typedclass.exceptions import TypedClassError, TypedClassValidationError
from typedclass.fields.data.base import BaseDataField
from typedclass.fields.special.base import BaseSpecialField


class Set(BaseSpecialField):
    @contract
    def process(self, name, value):
        """
        :type self: TypedClassBaseField
        :type name: str
        :type value: TypedClassAny
        :rtype: set|None
        """
        from typedclass.core import TypedClass
        # <-- circular import

        if self.required is False and value is None:
            return

        if isinstance(value, (set, frozenset, tuple, list)):
            converted_value = set()
            for entry in value:
                try:
                    if isinstance(entry, self.cls):
                        converted_value.add(entry)
                    elif isinstance(entry, dict) and issubclass(self.cls, TypedClass):
                        f_instance = self.cls(**entry)
                        converted_value.add(f_instance)
                    elif issubclass(self.cls, BaseDataField):
                        f_instance = self.cls()
                        _converted = f_instance.process(
                            name=name,
                            value=entry,
                        )
                        converted_value.add(_converted)
                    else:
                        raise TypedClassValidationError()
                except TypedClassValidationError:
                    raise TypedClassValidationError(
                        '{name}: element "{value}" is not instance of {cls}'.format(
                            name=name,
                            value=entry,
                            cls=self.cls,
                        )
                    )
            return converted_value
        else:
            raise TypedClassValidationError(
                '{name} is not set / frozenset / list / tuple of {cls}'.format(
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

        entries_processed = set()

        for entry in value:
            if entry in entries_processed:
                continue

            if isinstance(entry, self.cls):
                result.append(entry.simplify())
                entries_processed.add(entry)
            elif issubclass(self.cls, BaseDataField):
                f_instance = self.cls()
                simplified = f_instance.simplify(entry)
                result.append(simplified)
                entries_processed.add(entry)
            else:
                raise TypedClassError('Unsupported type')

        # ATTENTION!
        # we can't use "set" for unhashable types like dicts,
        # so we just use tuple here for simplify purpose
        return tuple(result)

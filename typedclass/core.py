from collections import namedtuple

from contracts import contract

from typedclass import fields as f
from typedclass.exceptions import TypedClassError, TypedClassValidationError
from typedclass.fields.base import BaseField
from typedclass.serializers.simple import SimpleSerializer


@contract
def _get_ignored_fields_frozen(bases, classdict):
    """
    :type bases: tuple
    :type classdict: dict
    :rtype: TypedClassFrozenset
    """
    ignored_fields = set()

    for base_class in bases:
        if issubclass(base_class, TypedClass):
            ignored_fields.update(base_class._ignored_fields_internal)

    for field in classdict.get('__ignored_fields__', ()):
        ignored_fields.add(field)

    return frozenset(ignored_fields)


@contract
def _is_field(value):
    """
    :type value: TypedClassAny
    :rtype: bool
    """
    return isinstance(value, BaseField)


@contract
def _get_fields(ignored_fields_frozen, bases, classdict):
    """
    :type ignored_fields_frozen: TypedClassFrozenset
    :type bases: tuple
    :type classdict: dict
    :rtype: dict
    """
    fields = {}

    for base_class in bases:
        for attr_name in dir(base_class):
            if attr_name in ignored_fields_frozen:
                continue

            attr_value = getattr(base_class, attr_name)

            if _is_field(attr_value):
                fields[attr_name] = attr_value

    for attr_name, attr_value in classdict.items():
        if attr_name in ignored_fields_frozen:
            continue

        if _is_field(attr_value):
            fields[attr_name] = attr_value

    return fields


class _Meta(type):
    @contract
    def __new__(mcs, name, bases, classdict):
        """
        return instance of TypedClass

        :type mcs: TypedClassMeta
        :type name: str
        :type bases: tuple
        :type classdict: dict
        """
        if bases:
            ignored_fields_frozen = _get_ignored_fields_frozen(bases, classdict)
            fields = _get_fields(ignored_fields_frozen, bases, classdict)
            fields_keys = fields.keys()

            fields_frozen = namedtuple('Fields', fields_keys)
            for field_name, field_class in fields.items():
                setattr(fields_frozen, field_name, field_class)

            classdict['_ignored_fields_internal'] = ignored_fields_frozen
            classdict['_fields'] = fields_frozen
            classdict['_storage_cls'] = namedtuple('Data', fields_keys)

        return super().__new__(mcs, name, bases, classdict)


class TypedClass(metaclass=_Meta):
    __slots__ = ('_data', )
    __ignored_fields__ = ()
    _ignored_fields_internal = frozenset()

    @contract
    def __init__(self, **raw_data):
        """
        :type self: TypedClass
        :type raw_data: dict
        :rtype: None
        """
        data = {}
        for field_name in self._fields._fields:
            field_value = raw_data.get(field_name)
            field = getattr(self._fields, field_name)
            field.process_base(
                name=field_name,
                value=field_value,
            )
            field_value = field.process(
                name=field_name,
                value=field_value,
            )
            data[field_name] = field_value

        _data = self._storage_cls(**data)
        object.__setattr__(self, '_data', _data)

    @contract
    def __getattribute__(self, name):
        """
        :type self: TypedClass
        :type name: str
        :rtype: TypedClassAny
        """
        result = super().__getattribute__(name)

        if isinstance(result, BaseField):
            return getattr(self._data, name)

        return result

    @contract
    def __setattr__(self, key, value):
        """
        :type self: TypedClass
        :type key: str
        :type value: TypedClassAny
        :rtype: None
        """
        raise TypedClassError('TypedClass is immutable')

    @contract
    def __eq__(self, other):
        """
        :type self: TypedClass
        :type other: TypedClassAny
        :rtype: bool|TypedClassNotImplemented
        """
        if isinstance(other, self.__class__):
            return self._data == other._data

        return NotImplemented

    @contract
    def __ne__(self, other):
        """
        :type self: TypedClass
        :type other: TypedClassAny
        :rtype: bool|TypedClassNotImplemented
        """
        if isinstance(other, self.__class__):
            return not self.__eq__(other)

        return NotImplemented

    @contract
    def __hash__(self):
        """
        :type self: TypedClass
        :rtype: int
        """
        return hash(self._data)

    def __repr__(self):
        return '{0}(**{1})'.format(self.__class__.__name__, self.dumps())

    @contract
    def items(self):
        """
        :type self: TypedClass
        :rtype: Iterable
        """
        return ((field_name, getattr(self._data, field_name)) for field_name in self._data._fields)

    @contract
    def update(self, **raw_data):
        """
        :type self: TypedClass
        :type raw_data: dict
        :rtype: TypedClass
        """
        data = {}

        for key in self._data._fields:
            value = raw_data.get(key) or getattr(self._data, key)
            data[key] = value

        return self.__class__(**data)

    @contract
    def convert_to(self, new_cls):
        """
        :type self: TypedClass
        :type new_cls: TypedClassCls
        :rtype: TypedClass
        """
        return new_cls(**self.to_dict())

    @contract
    def simplify(self):
        """
        :type self: TypedClass
        :rtype: dict
        """
        result = {}

        for key, value in self.items():
            field = getattr(self._fields, key)
            result[key] = field.simplify(value)

        return result

    @contract
    def to_dict(self):
        """
        :type self: TypedClass
        :rtype: dict
        """
        result = {}

        for key, value in self.items():
            field = getattr(self._fields, key)

            if value is not None:
                if isinstance(field, f.Ref):
                    value = value.to_dict()
                elif isinstance(field, f.List) and issubclass(field.cls, TypedClass):
                    converted_value = []
                    for val in value:
                        converted_value.append(val.to_dict())

                    value = converted_value

            result[key] = value

        return result

    @contract
    def dumps(self, serializer=SimpleSerializer):
        """
        :type self: TypedClass
        :type serializer: TypedClassBaseSerializerCls
        :rtype: str|TypedClassBytes
        """
        return serializer.dumps(self)

    @classmethod
    @contract
    def loads(cls, data, serializer=SimpleSerializer):
        """
        :type cls: TypedClassCls
        :type data: str|TypedClassBytes
        :type serializer: TypedClassBaseSerializerCls
        :rtype: TypedClass
        """
        try:
            return serializer.loads(cls, data)
        except ValueError:
            raise TypedClassValidationError('load data error')

    @contract
    def to_string(self):
        """
        :type self: TypedClass
        :rtype: str
        """
        return self.dumps()

    @classmethod
    @contract
    def from_string(cls, data_str):
        """
        :type data_str: str
        :rtype: TypedClass
        """
        return cls.loads(data_str)

    @classmethod
    @contract
    def gen_html(cls, only_div=False):
        """
        :type cls: TypedClassCls
        :type only_div: bool
        :rtype: str
        """
        from typedclass.html.render import gen_html
        return gen_html(cls, only_div=only_div)

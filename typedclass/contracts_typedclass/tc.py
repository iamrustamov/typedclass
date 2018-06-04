from contracts import new_contract


@new_contract
def TypedClass(x):
    from typedclass.core import TypedClass
    return isinstance(x, TypedClass)


@new_contract
def TypedClassBaseDataField(x):
    from typedclass.fields.data.base import BaseDataField
    return isinstance(x, BaseDataField)


@new_contract
def TypedClassMeta(x):
    from typedclass.core import _Meta
    return issubclass(x, _Meta)


@new_contract
def TypedClassBaseFieldCls(x):
    from typedclass.fields.base import BaseField
    return isinstance(x, type) and issubclass(x, BaseField)


@new_contract
def TypedClassCls(x):
    from typedclass.core import _Meta
    return isinstance(x, _Meta)


@new_contract
def TypedClassBaseSerializerCls(x):
    from typedclass.serializers.base import BaseSerializer
    return issubclass(x, BaseSerializer)


@new_contract
def TypedClassBaseField(x):
    from typedclass.fields.base import BaseField
    return isinstance(x, BaseField)


@new_contract
def TypedClassHTML(x):
    from typedclass.html.defs import TypedClassHTML
    return isinstance(x, TypedClassHTML)


@new_contract
def TypedClassHTMLField(x):
    from typedclass.html.defs import TypedClassHTMLField
    return isinstance(x, TypedClassHTMLField)


@new_contract
def TypedClassHTMLFieldProperties(x):
    from typedclass.html.defs import TypedClassHTMLFieldProperties
    return isinstance(x, TypedClassHTMLFieldProperties)

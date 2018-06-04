from decimal import Decimal

from contracts import contract
from typedclass import fields as f
from typedclass.core import TypedClass
from typedclass.html.defs import TypedClassHTML, TypedClassHTMLEntry, TypedClassHTMLField, TypedClassHTMLFieldProperties
from orderedset import OrderedSet


@contract
def _gen_typedclass_html_field_properties(field):
    """
    :type field: TypedClassBaseField
    :rtype: TypedClassHTMLFieldProperties
    """
    if isinstance(field, (f.Decimal, f.Int, f.Float)):
        if field.min_value is not None:
            min_value = Decimal(field.min_value)
        else:
            min_value = None

        if field.max_value is not None:
            max_value = Decimal(field.max_value)
        else:
            max_value = None

        properties = TypedClassHTMLFieldProperties(**{
            'required': field.required,
            'comment': field.comment,
            'min_value': min_value,
            'max_value': max_value,
        })
    elif isinstance(field, f.String):
        properties = TypedClassHTMLFieldProperties(**{
            'required': field.required,
            'comment': field.comment,
            'min_length': field.min_length,
            'max_length': field.max_length,
            'choices': field.choices,
        })
    elif isinstance(field, f.TypedMap):
        properties = TypedClassHTMLFieldProperties(**{
            'required': field.required,
            'comment': field.comment,
            'key': field.key.__class__.__name__,
            'value': field.value.__class__.__name__,
        })
    elif isinstance(field, (f.List, f.Ref, f.Set)):
        properties = TypedClassHTMLFieldProperties(**{
            'required': field.required,
            'comment': field.comment,
            'cls_name': field.cls.__name__,
        })
    else:
        properties = TypedClassHTMLFieldProperties(**{
            'required': field.required,
            'comment': field.comment,
        })
    return properties


@contract
def _gen_typedclass_html_field(field_name, field):
    """
    :type field_name: str
    :type field: TypedClassBaseField
    :rtype: TypedClassHTMLField
    """
    properties = _gen_typedclass_html_field_properties(field)
    html_field = TypedClassHTMLField(**{
        'name': field_name,
        'ftype': field.__class__.__name__,
        'properties': properties,
    })
    return html_field


@contract
def _gen_classes(cls):
    """
    returns OrderedSet of TypedClassCls

    :type cls: TypedClassCls
    :rtype: OrderedSet
    """
    classes = OrderedSet([cls])
    for field_name in cls._fields._fields:
        field = getattr(cls, field_name)

        if hasattr(field, 'cls') and issubclass(field.cls, TypedClass):
            classes_extra = _gen_classes(field.cls)
            classes = classes.union(classes_extra)

    return classes


@contract
def gen_typedclass_html(cls):
    """
    :type cls: TypedClassCls
    :rtype: TypedClassHTML
    """
    classes = _gen_classes(cls)
    entries = []

    for cls in classes:
        fields = []
        for field_name in cls._fields._fields:
            field = getattr(cls, field_name)
            html_field = _gen_typedclass_html_field(field_name, field)
            fields.append(html_field)

        entry = TypedClassHTMLEntry(**{
            'class_name': cls.__name__,
            'fields': fields,
        })
        entries.append(entry)

    typedclass_html = TypedClassHTML(**{
        'entries': entries,
    })
    return typedclass_html

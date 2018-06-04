from typedclass import fields as f
from typedclass.core import TypedClass


class TypedClassHTMLFieldProperties(TypedClass):
    # base:
    required = f.Bool()
    comment = f.String(required=False)

    # digital only:
    min_value = f.Decimal(required=False)
    max_value = f.Decimal(required=False)

    # string only:
    min_length = f.Int(required=False)
    max_length = f.Int(required=False)
    choices = f.List(f.String, required=False)

    # typedmap only:
    key = f.String(min_length=1, required=False)
    value = f.String(min_length=1, required=False)

    # special only:
    cls_name = f.String(min_length=1, required=False)


class TypedClassHTMLField(TypedClass):
    name = f.String(min_length=1)
    ftype = f.String(min_length=1)
    properties = f.Ref(TypedClassHTMLFieldProperties)


class TypedClassHTMLEntry(TypedClass):
    class_name = f.String(min_length=1)
    fields = f.List(TypedClassHTMLField)


class TypedClassHTML(TypedClass):
    entries = f.List(TypedClassHTMLEntry)

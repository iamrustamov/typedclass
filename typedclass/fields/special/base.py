from contracts import contract

from typedclass.fields.base import BaseField


# noinspection PyAbstractClass
class BaseSpecialField(BaseField):
    @contract
    def __init__(self, cls, required=True, comment=None):
        """
        :type self: TypedClassBaseField
        :type cls: TypedClassBaseFieldCls|TypedClassCls
        :type required: bool
        :type comment: str|None
        :rtype: None
        """
        super().__init__(required=required, comment=comment)
        self.cls = cls

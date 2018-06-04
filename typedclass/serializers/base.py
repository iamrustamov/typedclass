from contracts import contract


class BaseSerializer(object):
    @staticmethod
    @contract
    def dumps(typedclass):
        """
        :type typedclass: TypedClass
        :rtype: str|TypedClassBytes
        """
        raise NotImplementedError

    @staticmethod
    @contract
    def loads(typedclass_cls, data):
        """
        :type typedclass_cls: TypedClassCls
        :type data: str|TypedClassBytes
        :rtype: TypedClass
        """
        raise NotImplementedError

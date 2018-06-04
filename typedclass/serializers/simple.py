from contracts import contract
import ujson

from typedclass.serializers.base import BaseSerializer


class SimpleSerializer(BaseSerializer):
    @staticmethod
    @contract
    def dumps(typedclass):
        """
        :type typedclass: TypedClass
        :rtype: str
        """
        return ujson.dumps(typedclass.simplify())

    @staticmethod
    @contract
    def loads(typedclass_cls, data):
        """
        :type typedclass_cls: TypedClassCls
        :type data: str
        :rtype: TypedClass
        """
        raw_data = ujson.loads(data)
        return typedclass_cls(**raw_data)

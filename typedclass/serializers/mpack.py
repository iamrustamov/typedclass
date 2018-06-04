from contracts import contract
import msgpack

from typedclass.serializers.base import BaseSerializer


class MsgpackSerializer(BaseSerializer):
    @staticmethod
    @contract
    def dumps(typedclass):
        """
        :type typedclass: TypedClass
        :rtype: TypedClassBytes
        """
        return msgpack.dumps(typedclass.simplify())

    @staticmethod
    @contract
    def loads(typedclass_cls, data):
        """
        :type typedclass_cls: TypedClassCls
        :type data: TypedClassBytes
        :rtype: TypedClass
        """
        raw_data = msgpack.loads(data, encoding='utf-8')
        return typedclass_cls(**raw_data)

from typedclass.core import TypedClass
from typedclass.serializers.base import BaseSerializer


class Data(TypedClass):
    pass


def test_dumps():
    data = Data(**{})

    error = None
    try:
        data.dumps(serializer=BaseSerializer)
    except NotImplementedError as exc:
        error = exc

    assert error


def test_loads():
    error = None
    try:
        Data.loads('dumped', serializer=BaseSerializer)
    except NotImplementedError as exc:
        error = exc

    assert error

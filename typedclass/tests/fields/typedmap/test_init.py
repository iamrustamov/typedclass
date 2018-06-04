from typedclass import fields as f
from typedclass.exceptions import TypedClassError


def test_key_incorrect():
    error = None
    try:
        f.TypedMap(f.Bool(), f.Bool())
    except TypedClassError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'key type "String" supported only'

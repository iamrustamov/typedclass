from typedclass.fields.base import BaseField


def test_process_not_implemented():
    field = BaseField()

    error = None

    try:
        field.process('field', 'value')
    except NotImplementedError as exc:
        error = exc

    assert error


def test_simplify_not_implemented():
    field = BaseField()

    error = None

    try:
        field.simplify('value')
    except NotImplementedError as exc:
        error = exc

    assert error

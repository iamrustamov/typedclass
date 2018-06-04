from typedclass.fields.data.f_bool.desimplifier import desimplifier_bool


def test_not_str():
    result = desimplifier_bool(True)
    assert result is True


def test_false():
    result = desimplifier_bool('false')
    assert result is False


def test_0():
    result = desimplifier_bool('0')
    assert result is False


def test_true():
    result = desimplifier_bool('true')
    assert result is True


def test_1():
    result = desimplifier_bool('1')
    assert result is True

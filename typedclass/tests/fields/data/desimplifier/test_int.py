from typedclass.fields.data.f_int.desimplifier import desimplifier_int


def test_simplified():
    result = desimplifier_int('12345')
    assert result == 12345


def test_not_simplified():
    result_ok = 12345
    result = desimplifier_int(result_ok)
    assert result == result_ok

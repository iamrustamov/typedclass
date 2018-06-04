import string

from typedclass import fields as f
from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.data.f_string_email.validator import validator_string_email


def _test(value):
    f_string_email = f.StringEmail()

    error = None
    try:
        validator_string_email(f_string_email, value)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not a string email'


def test_not_string_email():
    # not str:
    _test(1)

    # empty str:
    _test('')

    # len > 255
    _test(string.ascii_letters * 5)

    # @ > 1
    _test('1@1@1.com')

    # ..
    _test('1@1..com')

    # regexp
    _test('1.com')


def test_ok():
    f_string_email = f.StringEmail()

    validator_string_email(f_string_email, '1@1.com')
    validator_string_email(f_string_email, '1+1@1.com')
    validator_string_email(f_string_email, 'test@зенхотелс.рф')

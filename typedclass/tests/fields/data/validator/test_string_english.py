from typedclass import fields as f
from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.data.f_string_english.validator import validator_string_english


def test_error():
    f_string_english = f.StringEnglish()

    error = None
    try:
        validator_string_english(f_string_english, 'ф')
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not a string english'


def test_error_not_str():
    f_string_english = f.StringEnglish()

    error = None
    try:
        validator_string_english(f_string_english, 1)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'Not a string english'


def test_ok():
    f_string_english = f.StringEnglish()

    validator_string_english(f_string_english, 'foo')
    validator_string_english(f_string_english, 'a b c')
    validator_string_english(f_string_english, 'abc123!#$%\()*+,-./:;&=?@[\\]^_`{|}~')

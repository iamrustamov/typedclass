from contracts import contract
import string

from typedclass.exceptions import TypedClassValidationError


@contract
def validator_string_english(field, value):
    """
    :type field: TypedClassBaseDataField
    :rtype: None
    """
    error_msg = 'Not a string english'

    if not isinstance(value, str):
        raise TypedClassValidationError(error_msg)

    # ATTENTION!
    # don't forget about spaces!
    allowed_chars = string.ascii_letters + string.digits + "!#$%\()*+,-./:;&=?@[\\]^_`{|}~ "

    for character in value:
        if character not in allowed_chars:
            raise TypedClassValidationError(error_msg)

    return

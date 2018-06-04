from contracts import contract
import re

from typedclass.exceptions import TypedClassValidationError


_EMAIL_RE = r'^(([a-z0-9\._-]+){0,1}(\+){0,1}([a-z0-9\._-]+){0,1}([a-z0-9_-]+){1}@(.+)\.(.{2,30}))$'


@contract
def validator_string_email(field, value):
    """
    :type field: TypedClassBaseDataField
    :rtype: None
    """
    error_msg = 'Not a string email'

    if not isinstance(value, str):
        raise TypedClassValidationError(error_msg)

    if not len(value) < 255:
        raise TypedClassValidationError(error_msg)

    if value.count('@') > 1:
        raise TypedClassValidationError(error_msg)

    if '..' in value:
        raise TypedClassValidationError(error_msg)

    if re.search(_EMAIL_RE, value, re.I):
        return

    raise TypedClassValidationError(error_msg)

from contracts import contract
import datetime as dt

from typedclass.exceptions import TypedClassValidationError


@contract
def desimplifier_datetime(value):
    """
    :type value: TypedClassAny
    :rtype: TypedClassDatetime|TypedClassAny
    """
    if isinstance(value, str):
        try:
            return dt.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S:%f')
        except ValueError:
            pass

        # ATTENTION!
        # all formats below are deprecated!
        # in future versions of typedclass this code will be deleted!
        # TODO: deprecated, remove after implementing custom format in f.DateTime
        try:
            return dt.datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ')
        except ValueError:
            pass

        try:
            return dt.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
        except ValueError:
            pass

        try:
            return dt.datetime.strptime(value, '%Y-%m-%dT%H:%M')
        except ValueError:
            raise TypedClassValidationError('Not a datetime')

    return value

from contracts import contract

from typedclass.exceptions import TypedClassValidationError


class BaseField(object):
    @contract
    def __init__(self, required=True, comment=None):
        """
        :type self: TypedClassBaseField
        :type required: bool
        :type comment: str|None
        :rtype: None
        """
        self.required = required
        self.comment = comment

    @contract
    def process_base(self, name, value):
        """
        base validation for all fields

        value - external raw_data

        :type self: TypedClassBaseField
        :type name: str
        :type value: TypedClassAny
        :rtype: None
        """
        if self.required is True and value is None:
            raise TypedClassValidationError('value "{}" is required but None'.format(name))

    @contract
    def process(self, name, value):
        """
        validate & convert data if need
        for example:
        if we expect TypedClass instance and got dict from value
        convert it to TypedClass instance

        value - external raw_data

        returns converted value for data storage

        :type self: TypedClassBaseField
        :type name: str
        :type value: TypedClassAny
        :rtype: None
        """
        raise NotImplementedError

    @contract
    def simplify(self, value):
        """
        :type self: TypedClassBaseField
        :type value: TypedClassAny
        :rtype: None
        """
        raise NotImplementedError

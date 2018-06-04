from typedclass import fields as f
from typedclass.core import TypedClass


class Data(TypedClass):
    string1 = f.String()
    string2 = f.String()
    sensitive_data1 = f.String()
    sensitive_data2 = f.String()


class DataCleaned1(Data):
    __ignored_fields__ = (
        'sensitive_data1',
    )
    string3 = f.String(required=False)


class DataCleaned2(DataCleaned1):
    __ignored_fields__ = (
        'sensitive_data2',
        'sensitive_data3',
    )
    sensitive_data3 = f.String(required=False)
    string4 = f.String(required=False)


def test():
    string1 = 'string1 value'
    string2 = 'string2 value'
    sensitive_data1 = 'sensitive_data1 value'
    sensitive_data2 = 'sensitive_data2 value'
    raw_data = {
        'string1': string1,
        'string2': string2,
        'sensitive_data1': sensitive_data1,
        'sensitive_data2': sensitive_data2,
    }
    data = Data(**raw_data)
    assert data.string1 == string1
    assert data.string2 == string2
    assert data.sensitive_data1 == sensitive_data1
    assert data.sensitive_data2 == sensitive_data2

    data_cleaned = data.convert_to(DataCleaned2)
    assert isinstance(data_cleaned, DataCleaned2)
    assert data_cleaned.string1 == string1
    assert data_cleaned.string2 == string2
    assert data_cleaned.string3 is None
    assert data_cleaned.string4 is None

    error = None
    try:
        data_cleaned.sensitive_data1
    except AttributeError as exc:
        error = exc

    msg = str(error)
    assert msg == "'Data' object has no attribute 'sensitive_data1'"

    error2 = None
    try:
        data_cleaned.sensitive_data2
    except AttributeError as exc:
        error2 = exc

    msg2 = str(error2)
    assert msg2 == "'Data' object has no attribute 'sensitive_data2'"

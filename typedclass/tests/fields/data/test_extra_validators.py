import datetime as dt
from decimal import Decimal as pyDecimal

from typedclass.exceptions import TypedClassValidationError
from typedclass.fields.data.f_date.core import Date
from typedclass.fields.data.f_bool.core import Bool
from typedclass.fields.data.f_datetime.core import DateTime
from typedclass.fields.data.f_decimal.core import Decimal
from typedclass.fields.data.f_int.core import Int
from typedclass.fields.data.f_string.core import String
from typedclass.fields.data.f_time.core import Time


def test_bool():
    def _true_validator(field, value):
        if value is False:
            raise TypedClassValidationError('Bool is not True')

    f_bool = Bool(extra_validators=(_true_validator, ))

    # correct one
    f_bool.process(name='f_bool', value=True)

    # extra validator error
    error = None
    try:
        f_bool.process(name='f_bool', value=False)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'f_bool: Bool is not True'


def test_datetime():
    def _future_validator(field, value):
        if value < dt.datetime.now():
            raise TypedClassValidationError('Datetime is not in future')

    f_datetime = DateTime(extra_validators=(_future_validator, ))

    # correct one
    f_datetime.process(name='f_datetime', value=dt.datetime.now() + dt.timedelta(days=1))

    # extra validator error
    error = None
    try:
        f_datetime.process(name='f_datetime', value=dt.datetime.now())
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'f_datetime: Datetime is not in future'


def test_date():
    def _future_validator(field, value):
        if value < dt.date.today():
            raise TypedClassValidationError('Date is not in future')

    f_date = Date(extra_validators=(_future_validator, ))

    # correct one
    f_date.process(name='f_date', value=dt.date.today() + dt.timedelta(days=1))

    # extra validator error
    error = None
    try:
        f_date.process(name='f_date', value=dt.date.today() - dt.timedelta(days=1))
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'f_date: Date is not in future'


def test_decimal():
    def _positive_validator(field, value):
        if value < pyDecimal('0'):
            raise TypedClassValidationError('Decimal is negative')

    f_decimal = Decimal(extra_validators=(_positive_validator, ))

    # correct one
    f_decimal.process(name='f_decimal', value=pyDecimal('0.01'))

    # extra validator error
    error = None
    try:
        f_decimal.process(name='f_decimal', value=pyDecimal('-0.01'))
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'f_decimal: Decimal is negative'


def test_int():
    def _positive_validator(field, value):
        if value < 0:
            raise TypedClassValidationError('Int is negative')

    f_int = Int(extra_validators=(_positive_validator, ))

    # correct one
    f_int.process(name='f_int', value=1)

    # extra validator error
    error = None
    try:
        f_int.process(name='f_int', value=-1)
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'f_int: Int is negative'


def test_string():
    def _card_number_validator(field, value):
        if not(12 <= len(value) <= 19):
            raise TypedClassValidationError('card number length must be 12-19 digits')

    f_string = String(extra_validators=(_card_number_validator, ))

    # correct one
    f_string.process(name='f_string', value='1234567890987654')

    # extra validator error
    error = None
    try:
        f_string.process(name='f_string', value='1234567890')
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'f_string: card number length must be 12-19 digits'


def test_time():
    def _morning_validator(field, value):
        # 06:00 <= time < 12:00
        if not(dt.time(6, 0) <= value < dt.time(12, 0)):
            raise TypedClassValidationError('Time is not in the morning range')

    f_time = Time(extra_validators=(_morning_validator, ))

    # correct1
    f_time.process(name='f_time', value=dt.time(6, 0))

    # correct2
    f_time.process(name='f_time', value=dt.time(11, 59, 59))

    # extra validator error
    error = None
    try:
        f_time.process(name='f_time', value=dt.time(12, 0, 1))
    except TypedClassValidationError as exc:
        error = exc

    assert error
    msg = str(error)
    assert msg == 'f_time: Time is not in the morning range'

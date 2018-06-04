from typedclass.fields.data.f_bool.core import Bool
from typedclass.fields.data.f_bool.desimplifier import desimplifier_bool
from typedclass.fields.data.f_bool.validator import validator_bool

from typedclass.fields.data.f_date.core import Date
from typedclass.fields.data.f_date.desimplifier import desimplifier_date
from typedclass.fields.data.f_date.simplifier import simplifier_date
from typedclass.fields.data.f_date.validator import validator_date

from typedclass.fields.data.f_datetime.core import DateTime
from typedclass.fields.data.f_datetime.desimplifier import desimplifier_datetime
from typedclass.fields.data.f_datetime.simplifier import simplifier_datetime
from typedclass.fields.data.f_datetime.validator import validator_datetime

from typedclass.fields.data.f_decimal.core import Decimal
from typedclass.fields.data.f_decimal.simplifier import simplifier_decimal
from typedclass.fields.data.f_decimal.desimplifier import desimplifier_decimal
from typedclass.fields.data.f_decimal.validator import validator_decimal

from typedclass.fields.data.f_int.core import Int
from typedclass.fields.data.f_int.desimplifier import desimplifier_int
from typedclass.fields.data.f_int.validator import validator_int

from typedclass.fields.data.f_string.core import String
from typedclass.fields.data.f_string.validator import validator_string

from typedclass.fields.data.f_time.core import Time
from typedclass.fields.data.f_time.desimplifier import desimplifier_time
from typedclass.fields.data.f_time.simplifier import simplifier_time
from typedclass.fields.data.f_time.validator import validator_time


def test_bool():
    assert Bool.simplifier is None
    assert Bool.desimplifier is desimplifier_bool
    assert Bool.validators == (validator_bool, )


def test_date():
    assert Date.simplifier is simplifier_date
    assert Date.desimplifier is desimplifier_date
    assert Date.validators == (validator_date, )


def test_datetime():
    assert DateTime.simplifier is simplifier_datetime
    assert DateTime.desimplifier is desimplifier_datetime
    assert DateTime.validators == (validator_datetime, )


def test_decimal():
    assert Decimal.simplifier is simplifier_decimal
    assert Decimal.desimplifier is desimplifier_decimal
    assert Decimal.validators == (validator_decimal, )


def test_int():
    assert Int.simplifier is None
    assert Int.desimplifier is desimplifier_int
    assert Int.validators == (validator_int, )


def test_string():
    assert String.simplifier is None
    assert String.desimplifier is None
    assert String.validators == (validator_string, )


def test_time():
    assert Time.simplifier is simplifier_time
    assert Time.desimplifier is desimplifier_time
    assert Time.validators == (validator_time, )

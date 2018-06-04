from contracts import new_contract
import datetime as dt


@new_contract
def TypedClassAny(x):
    return True


@new_contract
def TypedClassFrozenset(x):
    return isinstance(x, frozenset)


@new_contract
def TypedClassBytes(x):
    return isinstance(x, bytes)


@new_contract
def TypedClassNotImplemented(x):
    return x is NotImplemented


@new_contract
def TypedClassDate(x):
    return isinstance(x, dt.date)


@new_contract
def TypedClassDatetime(x):
    return isinstance(x, dt.datetime)


@new_contract
def TypedClassTime(x):
    return isinstance(x, dt.time)


@new_contract
def TypedClassDecimal(x):
    from decimal import Decimal
    return isinstance(x, Decimal)


@new_contract
def TypedClassFunc(x):
    return callable(x)

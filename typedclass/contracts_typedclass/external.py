from contracts import new_contract


@new_contract
def OrderedSet(x):
    from orderedset import OrderedSet
    return isinstance(x, OrderedSet)

from utils.sicp_data_abstraction import SICP

sicp = SICP()


def main():
    """Entry point"""
    test_last_pair()
    test_reverse()
    test_brooks()


def test_brooks():
    # A list of 2 value
    z = sicp.create_list(3, 4)
    print(brooks(plus_curried, z))

    z = sicp.create_list(brooks_curried, sicp.create_list(plus_curried, 3, 4))
    print(brooks_curried(z))

    z = sicp.create_list(
        brooks_curried,
        sicp.create_list(brooks_curried, sicp.create_list(plus_curried, 3, 4)),
    )
    print(brooks_curried(z))


def test_last_pair():
    # Empty
    x = sicp.create_list()
    print(last_pair(x))

    # A list of single value (pair)
    y = sicp.create_list(1)
    print(last_pair(y))

    # A list of multiple values
    z = sicp.create_list(32, 432, 2)
    print(last_pair(z))


def test_reverse():
    # Empty
    x = sicp.create_list()
    print(reverse(x))

    # A list of single value (pair)
    y = sicp.create_list(1)
    print(reverse(y))

    # A list of multiple values
    z = sicp.create_list(1, 2)
    print(reverse(z))


def last_pair(items):
    """receive a list and return a list contains only last element from previous list"""
    # if argument itself is empty list or None
    if sicp.is_none(items):
        return items

    # if it's the last element of list, then return the list itself
    # (because essentially a list of 1 element is just a pair)
    elif sicp.is_none(sicp.tail(items)):
        return items

    # otherwise, reduce the size of list by one
    # sequentially (remove it's head)
    else:
        return last_pair(sicp.tail(items))


def reverse(items):
    """reverse the list"""
    if sicp.is_none(items):
        return None
    else:
        return sicp.append(reverse(sicp.tail(items)), sicp.pair(sicp.head(items), None))


def plus_curried(x):
    """example of currying concept"""
    return lambda y: x + y


def brooks(f, items):
    """application of currying concept + high order function"""
    if sicp.is_none(items):
        return f
    else:
        return brooks(f(sicp.head(items)), sicp.tail(items))


def brooks_curried(items):
    return brooks(sicp.head(items), sicp.tail(items))


if __name__ == "__main__":
    main()

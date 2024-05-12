from chp2.sequences import reverse
from utils.sicp_data_abstraction import SICP

sicp = SICP()


def main():
    # test_scale_list()
    # test_map()
    # test_square_list_iter()
    test_for_each()


def scale_list(items, factor):
    if sicp.is_none(items):
        return None
    else:
        return sicp.pair(
            sicp.head(items) * factor, scale_list(sicp.tail(items), factor)
        )


def test_scale_list():
    # Empty
    x = sicp.create_list()
    print(scale_list(x, 2))

    # A pair / list single element
    y = sicp.create_list(1)
    print(scale_list(y, 2))

    # list of multi element
    z = sicp.create_list(1, 2, 3)
    print(scale_list(z, 2))


def map(func, items):
    if sicp.is_none(items):
        return None
    else:
        return sicp.pair(func(sicp.head(items)), map(func, sicp.tail(items)))


def test_map():
    # Empty
    x = sicp.create_list()
    print(map(lambda n: n * 2, x))

    # A pair / list single element
    y = sicp.create_list(1)
    print(map(lambda n: n * 2, y))

    # list of multi element
    z = sicp.create_list(1, 2, 3)
    print(map(lambda n: n * 2, z))


def square_list_iter(items):
    def iter(things, answer, is_first):
        if sicp.is_none(things):
            return answer

        # This is only for first element
        if is_first:
            return iter(
                sicp.tail(things),
                sicp.pair(square(sicp.head(things)), answer),
                not is_first,
            )

        # After first element, the rest of element will be go here
        return iter(
            sicp.tail(things),
            sicp.append(answer, sicp.pair(square(sicp.head(things)), None)),
            is_first,
        )

    return iter(items, None, True)


def square(x):
    return x**2


def test_square_list_iter():
    # Empty
    x = sicp.create_list()
    print(square_list_iter(x))

    # One element
    y = sicp.create_list(2)
    print(square_list_iter(y))

    # Two element
    z = sicp.create_list(2, 5)
    print(square_list_iter(z))

    # Multi element
    a = sicp.create_list(2, 4, 5, 10)
    print(square_list_iter(a))


def for_each(func, items):
    if sicp.is_none(items):
        return None
    else:
        func(sicp.head(items))
        return for_each(func, sicp.tail(items))


def test_for_each():
    # Multi element
    a = sicp.create_list(2, 4, 5, 10)
    print(for_each(lambda n: sicp.print(n), a))


if __name__ == "__main__":
    main()

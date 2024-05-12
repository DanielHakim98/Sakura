from utils.sicp_data_abstraction import SICP

sicp = SICP()


def main():
    """Entry point"""

    # # Is empty list
    # empty = sicp.create_list()
    # print(fringe(empty))

    # # Is a pair
    # pair = sicp.pair(1, 2)
    # print(fringe(pair))

    # Is a list
    arr = sicp.create_list(1, 2)
    print(fringe(arr))

    # # Is a tree
    tree = sicp.create_list(sicp.create_list(1, 2), sicp.create_list(3, 4))
    print(fringe(tree))

    ## Is not a list
    item = 2
    print(fringe(item))


def reverse(items):
    """reverse a list recursively"""
    if sicp.is_none(items):
        return None

    return sicp.append(reverse(sicp.tail(items)), sicp.pair(sicp.head(items), None))


def deep_reverse(items):
    """reverse a list recursively. including the if an element is a pair"""
    if sicp.is_none(items):
        return None

    elif sicp.is_pair(items):
        return sicp.append(
            deep_reverse(sicp.tail(items)),
            sicp.pair(deep_reverse(sicp.head(items)), None),
        )

    return items


def fringe(items):
    """accept sequence or tree and return list whose leaves of the tree arranged in left-to-right order"""

    if sicp.is_none(items):
        return None
    elif sicp.is_pair(items):
        # print("is a pair")
        return sicp.append(fringe(sicp.head(items)), fringe(sicp.tail(items)))
    return sicp.create_list(items)


if __name__ == "__main__":
    main()

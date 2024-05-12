from utils.sicp_data_abstraction import SICP
from chp2.mapping import map as map_sicp

sicp = SICP()


def main():
    # test_map_tree()
    x = sicp.create_list(1)
    print(subsets(x))


def count_leaves(x):
    if sicp.is_none(x):
        return 0
    if not sicp.is_pair(x):
        return 1
    return count_leaves(sicp.head(x)) + count_leaves(sicp.tail(x))


def test_count_leaves():
    # Empty
    arg1 = sicp.create_list()
    print(count_leaves(arg1))

    # 1 element (1 leaf, 1 None)
    arg2 = sicp.create_list(4)
    print(count_leaves(arg2))

    # multi-element
    arg2 = sicp.create_list(4, 34)
    print(count_leaves(arg2))

    # tree
    arg2 = sicp.create_list(sicp.create_list(1, 2), 3)
    print(count_leaves(arg2))

    # list list list
    arg3 = sicp.create_list(1, sicp.create_list(2, sicp.create_list(3, 4)))
    print(count_leaves(arg3))


def reverse(items):
    """reverse the list"""
    # print(f"reverse({items})")
    if sicp.is_none(items):
        return None
    if sicp.is_pair(sicp.head(items)):
        return sicp.append(
            reverse(sicp.tail(items)), sicp.pair(reverse(sicp.head(items)), None)
        )
    else:
        return sicp.append(reverse(sicp.tail(items)), sicp.pair(sicp.head(items), None))


def test_reverse():
    # A list of multiple values
    z = sicp.create_list(sicp.create_list(1, 2), 3)
    print(reverse(z))

    a = sicp.create_list(sicp.create_list(1, 2), sicp.create_list(3, 4))
    print(reverse(a))


def make_mobile(left, right):
    return sicp.create_list(left, right)


def make_branch(length: int, structure):
    return sicp.create_list(length, structure)


def left_branch(mobile):
    return sicp.head(mobile)


def right_branch(mobile):
    return sicp.head(sicp.tail(mobile))


def branch_length(branch):
    return sicp.head(branch)


def branch_structure(branch):
    return sicp.head(sicp.tail(branch))


def is_weight(b):
    return isinstance(b, int) or isinstance(b, float)


def total_weigth(branch):
    if sicp.is_none(branch):
        return 0
    if is_weight(branch):
        return branch
    else:
        return total_weigth(sicp.head(branch)) + total_weigth(sicp.tail(branch))


def correct_total_weight(m):
    if sicp.is_none(m):
        return 0
    elif is_weight(m):
        return m
    else:
        return correct_total_weight(
            branch_structure(left_branch(m))
        ) + correct_total_weight(branch_structure(right_branch(m)))


def test_2_29_exercise():
    left = make_branch(2, 3)
    right = make_branch(7, 5)
    mobile2 = make_mobile(left, right)
    print(total_weigth(mobile2))
    print(correct_total_weight(mobile2))


def scale_tree(tree, factor):
    if sicp.is_none(tree):
        return None
    elif not sicp.is_pair(tree):
        return tree * factor
    else:
        return sicp.pair(
            scale_tree(sicp.head(tree), factor),
            scale_tree(sicp.tail(tree), factor),
        )


def test_scale_tree():
    # simple tree
    tr = sicp.create_list(
        sicp.create_list(1, 2),
        sicp.create_list(3, 4),
    )
    print(scale_tree(tr, 100))

    # complex tree
    print(
        scale_tree(
            sicp.create_list(
                1,
                sicp.create_list(2, sicp.create_list(3, 4), 5),
                sicp.create_list(6, 7),
            ),
            10,
        )
    )


def map_tree(func, tree):
    if sicp.is_none(tree):
        return None
    elif not sicp.is_pair(tree):
        return func(tree)
    else:
        return sicp.pair(
            map_tree(func, sicp.head(tree)),
            map_tree(func, sicp.tail(tree)),
        )


def test_map_tree():
    tree1 = sicp.create_list(
        sicp.create_list(1, 2),
        sicp.create_list(3, 4),
    )
    print(map_tree(lambda x: x**2, tree1))
    tree2 = sicp.create_list(
        1,
        sicp.create_list(2, sicp.create_list(3, 4), 5),
        sicp.create_list(6, 7),
    )
    print(map_tree(lambda x: x**2, tree2))


def subsets(s):
    if sicp.is_none(s):
        return sicp.create_list(None)
    else:
        rest = subsets(sicp.tail(s))
        print("rest: ", rest)
        return sicp.append(
            rest,
            map_sicp(lambda ele: sicp.pair(sicp.head(s), ele), rest),
        )


if __name__ == "__main__":
    main()

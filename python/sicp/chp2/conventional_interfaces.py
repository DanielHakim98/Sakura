from typing import Callable
from utils.sicp_data_abstraction import SICP

sicp = SICP()


def filter_list(predicate: Callable, items):
    """construct element by condition"""
    if sicp.is_none(items):
        return None

    # check condition to filter based on predicate
    if predicate(sicp.head(items)):
        return sicp.pair(
            sicp.head(items),
            filter_list(
                predicate,
                sicp.tail(items),
            ),
        )
    # else, skip current head, go through remaining tail
    return filter_list(predicate, sicp.tail(items))


def test_filter_list():
    def is_even(n):
        return n % 2 == 0

    # Empty
    x = sicp.create_list()
    print(filter_list(is_even, x))

    # A list of single value (pair)
    y = sicp.create_list(1)
    print(filter_list(is_even, y))

    # A list of multiple values
    z = sicp.create_list(1, 2, 3, 4)
    print(filter_list(is_even, z))


def accumulate(op, initial, sequence):
    if sicp.is_none(sequence):
        return initial
    return op(
        sicp.head(sequence),
        accumulate(op, initial, sicp.tail(sequence)),
    )


def test_accumulate():
    def add(x, y):
        return x + y

    # Empty
    x = sicp.create_list()
    print(accumulate(add, 0, x))

    # A list of single value (pair)
    y = sicp.create_list(1)
    print(accumulate(add, 0, y))

    # A list of multiple values
    z = sicp.create_list(1, 2, 3, 4)
    print(accumulate(add, 0, z))


def enumerate_interval(low, high):
    if low > high:
        return None
    return sicp.pair(low, enumerate_interval(low + 1, high))


def test_enumerate_interval():
    print(enumerate_interval(1, 7))


def enumerate_tree(tree):
    if sicp.is_none(tree):
        return None
    # if tree is a leave, then return list with that element
    if not sicp.is_pair(tree):
        return sicp.create_list(tree)

    return sicp.append(
        enumerate_tree(sicp.head(tree)),
        enumerate_tree(sicp.tail(tree)),
    )


def test_enumerate_tree():
    t = sicp.create_list(
        1,
        sicp.create_list(2, sicp.create_list(3, 4)),
        5,
    )
    print(enumerate_tree(t))


def map_list(f, sequence):
    def op(x, y):
        return sicp.pair(f(x), y)

    return accumulate(op, None, sequence)


def test_map_list():
    # A list of multiple values
    z = sicp.create_list(1, 2, 3, 4)
    print(map_list(lambda x: x * 2, z))


def append(seq1, seq2):
    return accumulate(sicp.pair, seq2, seq1)


def test_append():
    s1 = sicp.create_list(1, 2)
    s2 = sicp.create_list(5, 6)
    print(append(s1, s2))


def length(seq):
    def count(_, y):
        return 1 + y

    return accumulate(count, 0, seq)


def test_length():
    seq = sicp.create_list(3, 4, 10)
    print(length(seq))


def horner_eval(x, coefficient_sequence):
    return accumulate(
        lambda this_coeff, higher_terms: this_coeff + x * higher_terms,
        0,
        coefficient_sequence,
    )


def test_hornel_eval():
    seq = sicp.create_list(1, 3, 0, 5, 0, 1)
    x = 2
    print(horner_eval(x, seq))


def count_leaves(t):
    # Method 1: expand tree become a list, then count element in list
    """
    EX:
    return accumulate(
        lambda x, y: y + 1,
        0,
        enumerate_tree(t),
    )
    """

    # Method 2: Divide and conquer, calculate total list within subtree then accumulate it
    def check_subtree(subt):
        # for every element within tree, check if it's a pair
        if not sicp.is_pair(subt):
            return 1
        return count_leaves(subt)

    return accumulate(lambda cur, total: cur + total, 0, map_list(check_subtree, t))


def test_count_leaves():
    tree = sicp.create_list(1, sicp.create_list(3, 4))
    print(count_leaves(tree))


def accumulate_n(reducer, accumulator, sequence):
    if sicp.is_none(sequence):
        return None
    return sicp.pair(
        accumulate(reducer, accumulator, map_list(sicp.head, sequence)),
        accumulate_n(
            reducer,
            accumulator,
            filter_list(
                lambda ele: not sicp.is_none(ele), map_list(sicp.tail, sequence)
            ),
        ),
    )


def test_accumulate_n():
    seq_seq = sicp.create_list(
        sicp.create_list(1, 2, 3),
        sicp.create_list(4, 5, 6),
        sicp.create_list(7, 8, 9),
        sicp.create_list(10, 11, 12),
    )
    print(accumulate_n(lambda x, y: x + y, 0, seq_seq))


def plus(x, y):
    return x + y


def times(x, y):
    return x * y


def dot_product(v, w):
    return accumulate(plus, 0, accumulate_n(times, 1, sicp.create_list(v, w)))


def test_dot_product():
    v = sicp.create_list(1, 3, -5)
    w = sicp.create_list(4, -2, -1)
    print(dot_product(v, w))


def matrix_times_vector(m, v):
    return map_list(lambda x: x * v, m)


def test_matrix_times_vector():
    pass


# v = [1,2] --> 1 x 2 matrix
# m = [[3], [4]] --> 2 x 1 matrix

# t = [1 * 3 + 2 * 4] --> 1 x 1 matrix


def flatmap(f, seq):
    return accumulate(sicp.append, None, map_list(f, seq))


def test_flatmap():
    def _sequence_of_pairs(i):
        return map_list(
            lambda j: sicp.create_list(i, j),
            enumerate_interval(1, i - 1),
        )

    def remove(item, sequence):
        return filter_list(lambda x: x != item, sequence)

    def permutations(s):
        if sicp.is_none(s):
            return sicp.create_list(None)
        return flatmap(
            lambda x: map_list(lambda p: sicp.pair(x, p), permutations(remove(x, s))),
            s,
        )

    print(permutations(enumerate_interval(1, 3)))


def main():
    """Entry point"""

    # test_append()
    # test_length()
    # test_hornel_eval()
    # test_count_leaves()
    # test_accumulate_n()
    # test_dot_product()
    test_flatmap()


if __name__ == "__main__":
    main()

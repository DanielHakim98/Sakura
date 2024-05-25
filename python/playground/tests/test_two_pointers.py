import unittest
from dataclasses import dataclass
from problems.two_pointers import (
    move_zeroes,
    threesum,
    two_sum_2,
    merge_sorted_array,
    valid_palindrome_2,
    max_area,
)


# class Test3Sum(unittest.TestCase):
#     def test_three_sum(self):
#         @dataclass
#         class TestCase:
#             name: str
#             input: list[int]
#             want: list[list[int]]

#         test_cases = [
#             TestCase(
#                 name="example 1",
#                 input=[-1, 0, 1, 2, -1, -4],
#                 want=[[-1, -1, 2], [-1, 0, 1]],
#             )
#         ]
#         for case in test_cases:
#             got = threesum(case.input)
#             self.assertEqual(
#                 got,
#                 case.want,
#                 f"\nFailed test '{case.name}'. got: '{got}', want: '{case.want}'.",
#             )


class TestTwoSum2(unittest.TestCase):
    def test_two_sum_2(self):
        @dataclass
        class TestCase:
            name: str
            input_1: list[int]
            input_2: int
            want: list[int]

        test_cases = [
            TestCase(
                name="example 1",
                input_1=[2, 7, 11, 15],
                input_2=9,
                want=[1, 2],
            )
        ]
        for case in test_cases:
            got = two_sum_2(case.input_1, case.input_2)
            self.assertEqual(
                got,
                case.want,
                f"\nFailed test '{case.name}'. got: '{got}', want: '{case.want}'.",
            )


class TestMergeSortedArray(unittest.TestCase):
    def test_merge_sorted_array(self):
        @dataclass
        class Params:
            nums1: list[int]
            m: int
            nums2: list[int]
            n: int

        @dataclass
        class TestCase:
            name: str
            inputs: Params
            want: list[int]

        test_cases = [
            TestCase(
                name="example 1",
                inputs=Params([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),
                want=[1, 2, 2, 3, 5, 6],
            ),
            TestCase(name="example 2", inputs=Params([1], 1, [], 0), want=[1]),
            TestCase(name="example 3", inputs=Params([0], 0, [1], 1), want=[1]),
            TestCase(name="example 4", inputs=Params([1, 0], 1, [2], 1), want=[1, 2]),
            TestCase(name="example 5", inputs=Params([2, 0], 1, [1], 1), want=[1, 2]),
        ]
        for case in test_cases:
            got = case.inputs.nums1
            merge_sorted_array(
                case.inputs.nums1, case.inputs.m, case.inputs.nums2, case.inputs.n
            )
            self.assertEqual(
                got,
                case.want,
                f"\nFailed test '{case.name}'. got: '{got}', want: '{case.want}'.",
            )


class TestValidPalindrome2(unittest.TestCase):
    def test_valid_palindrome_2(self):
        @dataclass
        class TestCase:
            name: str
            input: str
            want: bool

        test_cases = [
            TestCase(name="example 1", input="aba", want=True),
            TestCase(name="example 2", input="abca", want=True),
            TestCase(name="example 3", input="abc", want=False),
            TestCase(name="example 4", input="abbbbb", want=True),
            TestCase(name="example 4", input="eed", want=True),
        ]
        for case in test_cases:
            got = valid_palindrome_2(case.input)
            self.assertEqual(
                got,
                case.want,
                f"\nFailed test '{case.name}'. got: '{got}', want: '{case.want}'.",
            )


class TestMoveZeros(unittest.TestCase):
    def test_move_zeros(self):
        @dataclass
        class TestCase:
            name: str
            input: list[int]
            want: list[int]

        test_cases = [
            TestCase(name="example 1", input=[0, 1, 0, 3, 12], want=[1, 3, 12, 0, 0]),
            TestCase(name="example 2", input=[0], want=[0]),
            TestCase(name="example 3", input=[1, 2, 3], want=[1, 2, 3]),
            TestCase(
                name="example 4", input=[-4, -1, 0, 3, 7, 0], want=[-4, -1, 3, 7, 0, 0]
            ),
            TestCase(
                name="example 5",
                input=[-2, 0, 0, 0, -1, 0, 0, 3],
                want=[-2, -1, 3, 0, 0, 0, 0, 0],
            ),
        ]
        for case in test_cases:
            got = case.input
            move_zeroes(case.input)
            self.assertEqual(
                got,
                case.want,
                f"\nFailed test '{case.name}'. got: '{got}', want: '{case.want}'.",
            )


class TestContainerWithMostWater(unittest.TestCase):
    def test_example_1(self):
        input_ = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        got = max_area(input_)
        want = 49
        self.assertEqual(
            got,
            want,
            f"\nFailed test '{input_}'. got: '{got}', want: '{want}'.",
        )

    def test_example_2(self):
        input_ = [1, 1]
        got = max_area(input_)
        want = 1
        self.assertEqual(
            got,
            want,
            f"\nFailed test '{input_}'. got: '{got}', want: '{want}'.",
        )

    def test_example_3(self):
        input_ = [1, 2, 4, 3]
        got = max_area(input_)
        want = 4
        self.assertEqual(
            got,
            want,
            f"\nFailed test '{input_}'. got: '{got}', want: '{want}'.",
        )

    def test_example_4(self):
        input_ = [2, 3, 10, 5, 7, 8, 9]
        got = max_area(input_)
        want = 36
        self.assertEqual(
            got,
            want,
            f"\nFailed test '{input_}'. got: '{got}', want: '{want}'.",
        )


if __name__ == "__main__":
    unittest.main()

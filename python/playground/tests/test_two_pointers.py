import unittest
from dataclasses import dataclass
from problems.two_pointers import (
    threesum,
    two_sum_2,
    merge_sorted_array,
    valid_palindrome_2,
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


if __name__ == "__main__":
    unittest.main()

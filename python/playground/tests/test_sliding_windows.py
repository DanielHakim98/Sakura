from dataclasses import dataclass
import unittest
from problems.sliding_windows import (
    contain_duplicate_2,
    max_average_of_k_window,
    smallest_subarray,
    longest_substring_distinct_k,
    longest_non_repeat,
    longest_repeat_char_replace,
)


class TestAverageOfK(unittest.TestCase):
    def test_ok(self):
        arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
        k = 5
        got = max_average_of_k_window(arr, k)
        want = 3.6
        self.assertEqual(got, want)


class TestSmallestSubarray(unittest.TestCase):
    def test_ok(self):
        arr = [2, 1, 5, 2, 3, 2]
        k = 7
        got = smallest_subarray(arr, k)
        want = 2
        self.assertEqual(got, want)

    def test_not_ok(self):
        arr = [2, 4, 3]
        k = 7
        got = smallest_subarray(arr, k)
        want = 2
        self.assertEqual(got, want)


class TestLongestSubstringDistinctK(unittest.TestCase):
    def test_longest_substring_distinct_k(self):
        @dataclass
        class TestCase:
            name: str
            input: tuple[str, int]
            want: int

        test_cases = [
            TestCase(name="example 1", input=("araaci", 2), want=4),
            TestCase(name="example 2", input=("araaci", 1), want=2),
            TestCase(name="example 3", input=("cbbebi", 3), want=5),
            TestCase(name="example 4", input=("abbbbbbc", 2), want=7),
            TestCase(name="example 5", input=("abbbbbbc", 3), want=8),
            TestCase(name="example 6", input=("abcddefg", 3), want=4),
        ]

        for case in test_cases:
            got = longest_substring_distinct_k(*case.input)
            self.assertEqual(
                got,
                case.want,
                f"\nFailed test '{case.name}'. got: '{got}', want: '{case.want}'.",
            )


class TestLongestNonRepeatSubstring(unittest.TestCase):
    def test_longest_non_repeat(self):
        @dataclass
        class TestCase:
            name: str
            input: str
            want: int

        test_cases = [
            TestCase(name="example 1", input="aabccbb", want=3),
            TestCase(name="example 2", input="abbbb", want=2),
            TestCase(name="example 3", input="abccde", want=3),
        ]

        for case in test_cases:
            got = longest_non_repeat(case.input)
            self.assertEqual(
                got,
                case.want,
                f"\nFailed test '{case.name}'. got: '{got}', want: '{case.want}'.",
            )


class TestLongestRepeatingCharacterReplace(unittest.TestCase):
    def test_longest_repeat_char_replace(self):
        @dataclass
        class TestCase:
            name: str
            input: tuple[str, int]
            want: int

        test_cases = [
            TestCase(name="example 1", input=("ABAB", 2), want=4),
            TestCase(name="example 2", input=("AABABBA", 1), want=4),
        ]

        for case in test_cases:
            got = longest_repeat_char_replace(case.input[0], case.input[1])
            self.assertEqual(
                got,
                case.want,
                f"\nFailed test '{case.name}'. got: '{got}', want: '{case.want}'.",
            )


class TestContainsDuplicate2(unittest.TestCase):
    def test_contain_duplicate_2(self):
        @dataclass
        class TestCase:
            name: str
            input: tuple[list[int], int]
            want: bool

        test_cases = [
            TestCase(name="example 1", input=([1, 2, 3, 1], 3), want=True),
            TestCase(name="example 2", input=([1, 0, 1, 1], 1), want=True),
            TestCase(name="example 3", input=([1, 2, 3, 1, 2, 3], 2), want=False),
        ]
        for case in test_cases:
            got = contain_duplicate_2(case.input[0], case.input[1])
            self.assertEqual(
                got,
                case.want,
                f"\nFailed test '{case.name}'. got: '{got}', want: '{case.want}'.",
            )


if __name__ == "__main__":
    unittest.main()

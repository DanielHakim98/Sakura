import unittest
from dataclasses import dataclass
from problems.two_pointers import threesum, two_sum_2


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


if __name__ == "__main__":
    unittest.main()

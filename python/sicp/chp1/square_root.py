from typing import Any
from utils.sicp_data_abstraction import SICP

sicp = SICP()


def main():
    square_newton = {
        "quotient": lambda x, g: x / g,
        "adder": lambda g: g,
        "divider": lambda n: n / 2,
    }
    sqrt = PowerRoot(square_newton)
    print("answer: ", sqrt.root(4))

    cube_newton = {
        "quotient": lambda x, g: x / g**2,
        "adder": lambda g: 2 * g,
        "divider": lambda n: n / 3,
    }
    cbrt = PowerRoot(cube_newton)
    print("answer: ", cbrt.root(8))


class SquareRoot:
    def __init__(self):
        self.error_threshold = 0.0001

    def sqrt(self, num):
        return self.sqrt_iter(1, num)

    def sqrt_iter(self, guess, num):
        if self.is_good_enough(guess, num):
            return guess
        else:
            return self.sqrt_iter(self.improve(guess, num), num)

    def is_good_enough(
        self,
        guess,
        num,
    ):
        return (
            self.relative_error(guess, self.improve(guess, num)) < self.error_threshold
        )

    def relative_error(self, estimate, reference):
        return abs(estimate - reference) / reference

    def square(self, x):
        return x * x

    def improve(self, guess, x):
        return self.average(guess, x / guess)

    def average(self, x, y):
        return (x + y) / 2


class CubeRoot:
    def __init__(self):
        self.error_threshold = 0.00001

    def cbrt(self, num):
        return self.cbrt_iter(1, num)

    def cbrt_iter(self, guess, num):
        if self.is_good_enough(guess, num):
            return guess
        else:
            return self.cbrt_iter(self.improve(guess, num), num)

    def is_good_enough(self, guess, num):
        return (
            self.relative_error(guess, self.improve(guess, num)) < self.error_threshold
        )

    def relative_error(self, estimate, reference):
        return abs(estimate - reference) / reference

    def cube(self, x):
        return x * x * x

    def improve(self, guess, x):
        return self.divide_by_3(x / (guess * guess), 2 * guess)

    def divide_by_3(self, x, y):
        return (x + y) / 3


class PowerRoot:
    def __init__(self, newton_method: dict[str, Any]):
        self.error_threshold = 0.00001
        self.quotient = newton_method.get("quotient", lambda: None)
        self.adder = newton_method.get("adder", lambda: None)
        self.divider = newton_method.get("divider", lambda: None)

    def root(self, num):
        return self.root_iter(1, num)

    def root_iter(self, guess, num):
        if self.is_good_enough(guess, num):
            return guess
        else:
            return self.root_iter(self.improve(guess, num), num)

    def is_good_enough(self, guess, num):
        return (
            self.relative_error(guess, self.improve(guess, num)) < self.error_threshold
        )

    def relative_error(self, estimate, reference):
        return abs(estimate - reference) / reference

    def improve(self, guess, x):
        return self.divider(self.quotient(x, guess) + self.adder(guess))


if __name__ == "__main__":
    main()

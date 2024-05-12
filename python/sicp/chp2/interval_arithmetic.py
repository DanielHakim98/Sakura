from dataclasses import dataclass
from utils.sicp_data_abstraction import SICP

sicp = SICP()
make_interval = sicp.pair
lower_bound = sicp.head
upper_bound = sicp.tail


@dataclass
class Interval:
    """Class for representing interval object"""

    start: int
    end: int

    def lower_bound(self) -> int:
        return self.start

    def upper_bound(self) -> int:
        return self.end


def add_interval(x, y):
    return make_interval(
        lower_bound(x) + lower_bound(y), upper_bound(x) + upper_bound(y)
    )


def mul_interval(x, y):
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return make_interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))


def div_interval(x, y):
    return mul_interval(x, make_interval(1 / upper_bound(y), 1 / lower_bound(y)))


def sub_interval(x, y):
    return make_interval(
        lower_bound(x) - upper_bound(y), upper_bound(x) - lower_bound(y)
    )

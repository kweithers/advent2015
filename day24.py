from functools import reduce
from operator import mul
from itertools import combinations

INPUT = [1, 3, 5, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
         53, 59, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

TEST_INPUT = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]


class Sleigh:
    def __init__(self, weights: list[int], n: int) -> None:
        self.weights = weights
        self.w = sum(weights) // n

    def solve(self) -> int:
        for i in range(len(self.weights)):
            qes = [reduce(mul, c) for c in combinations(
                self.weights, i) if sum(c) == self.w]
            if qes:
                return min(qes)


def test_p1():
    s = Sleigh(TEST_INPUT, 3)
    assert s.solve() == 99


def test_p2():
    s = Sleigh(TEST_INPUT, 4)
    assert s.solve() == 44


s = Sleigh(INPUT, 3)
print("Part 1: ", s.solve())
s = Sleigh(INPUT, 4)
print("Part 2: ", s.solve())

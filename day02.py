from typing import List


class Present:
    def __init__(self, dimensions: List[str]):
        self.l = int(dimensions[0])
        self.w = int(dimensions[1])
        self.h = int(dimensions[2])

    def paper_needed(self) -> int:
        return 2 * self.l * self.w + 2 * self.w * self.h + 2 * self.h * self.l + self.smallest_side_area()

    def smallest_side_area(self) -> int:
        return min(self.l * self.w, self.w * self.h, self.h * self.l)

    def ribbon_needed(self) -> int:
        return self.l*self.w*self.h + sum([side+side for side in self.smallest_two_sides()])

    def smallest_two_sides(self) -> List[int]:
        dims = [self.l, self.w, self.h]
        dims.sort()
        return dims[0:2]


input = open("day02.txt").readlines()


def part1(input: List[str]) -> int:
    return sum([Present(line.split("x")).paper_needed() for line in input])


def test_part1():
    assert part1(["2x3x4"]) == 58
    assert part1(["1x1x10"]) == 43


print("Part 1:", part1(input))


def part2(input: List[str]) -> int:
    return sum([Present(line.split("x")).ribbon_needed() for line in input])


def test_part2():
    assert part2(["2x3x4"]) == 34
    assert part2(["1x1x10"]) == 14


print("Part 2:", part2(input))

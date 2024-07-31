from collections import defaultdict
from typing import List
INPUT = open('day18.txt').read().splitlines()
TEST_INPUT = open('day18test.txt').read().splitlines()


class Grid:
    def __init__(self, lines: List[str], part2: bool = False) -> None:
        self.grid = defaultdict(bool, self.create_grid(lines))
        self.rows = len(lines)
        self.columns = len(lines[0])
        self.part2 = part2

    def create_grid(self, lines: List[str]) -> dict[tuple[int, int], bool]:
        return {(y, x): char == '#' for y, line in enumerate(lines) for x, char in enumerate(line)}

    def new_state(self) -> None:
        self.grid = defaultdict(bool, {(y, x): self.num_neighbors_on(y, x) in [2, 3] if self.grid[(
            y, x)] else self.num_neighbors_on(y, x) == 3 for y in range(self.rows) for x in range(self.columns)})

    def num_neighbors_on(self, y: int, x: int) -> int:
        return sum(self.grid[(y+j, x+i)] for j in [-1, 0, 1] for i in [-1, 0, 1] if (j, i) != (0, 0))

    def turn_corners_on(self) -> None:
        for (y, x) in [(0, 0), (0, self.columns-1), (self.rows-1, 0), (self.rows-1, self.columns-1)]:
            self.grid[(y, x)] = True

    def step(self, n: int) -> None:
        for _ in range(n):
            if self.part2:
                self.turn_corners_on()
            self.new_state()
        if self.part2:
            self.turn_corners_on()


def test_p1():
    g = Grid(TEST_INPUT)
    g.step(4)
    assert sum(g.grid.values()) == 4


def test_p2():
    g = Grid(TEST_INPUT, part2=True)
    g.step(5)
    assert sum(g.grid.values()) == 17


g = Grid(INPUT)
g.step(100)
print("Part 1: ", sum(g.grid.values()))

g = Grid(INPUT, part2=True)
g.step(100)
print("Part 2: ", sum(g.grid.values()))

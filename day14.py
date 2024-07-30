from dataclasses import dataclass
from typing import List
from collections import defaultdict
INPUT = open('day14.txt').readlines()
TIME = 2503


@dataclass(frozen=True)
class Reindeer:
    name: str
    speed: int
    duration: int
    rest: int


class Herd:
    def __init__(self, lines: List[str]) -> None:
        self.reindeer: dict[str, Reindeer] = self.parse_lines(lines)

    def parse_lines(self, lines: List[str]) -> set[Reindeer]:
        s = set()
        for line in lines:
            tokens = line.split(',')
            s.add(Reindeer(tokens[0], int(tokens[1]),
                           int(tokens[2]), int(tokens[3])))
        return s

    def calculate_distance(self, r: Reindeer, time: int) -> int:
        total_loops = time // (r.duration + r.rest)
        loops_distance = total_loops * r.duration * r.speed

        remaining_time = min(time % (r.duration + r.rest), r.duration)
        last_distance = remaining_time * r.speed

        return loops_distance + last_distance

    def max_distance(self, time: int) -> int:
        return max((self.calculate_distance(r, time) for r in self.reindeer))

    def max_points(self, time: int) -> int:
        points: dict[str, int] = defaultdict(lambda: 0)
        distances: dict[str, int] = defaultdict(lambda: 0)

        for t in range(time):
            for r in self.reindeer:
                if t % (r.duration + r.rest) < r.duration:
                    distances[r.name] += r.speed

            for k in [k for (k, v) in distances.items() if v == max(distances.values())]:
                points[k] += 1
        return max(points.values())


def test():
    h = Herd(open('day14test.txt').readlines())
    assert h.max_distance(1000) == 1120
    assert h.max_points(1000) == 689


h = Herd(INPUT)
print("Part 1: ", h.max_distance(TIME))
print("Part 2: ", h.max_points(TIME))

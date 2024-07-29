from typing import List
from itertools import permutations
INPUT = open('day13.txt').readlines()


class DinnerTable:
    def __init__(self, lines: str, add_neutral_person: bool = False):
        self.lines = lines
        self.dct = {}
        self.people = set()
        self.add_neutral_person = add_neutral_person

    def parse_lines(self):
        for line in self.lines:
            tokens = line.rstrip('\n').split(' ')
            self.dct[(tokens[0], tokens[2])] = int(tokens[1])
            self.people.add(tokens[0])

    def calculate_happiness(self, seats: List[str]) -> int:
        happiness = 0
        for i, person in enumerate(seats):
            happiness += self.dct[(person, seats[(i+1) % len(seats)])]
            happiness += self.dct[(person, seats[(i-1) % len(seats)])]

        if self.add_neutral_person:
            return happiness - self.calculate_worst_pair(seats)
        return happiness

    def calculate_worst_pair(self, seats: List[str]) -> int:
        return min(self.dct[(person, seats[(i+1) % len(seats)])] +
                   self.dct[(seats[(i+1) % len(seats)], person)] for i, person in enumerate(seats))

    def calculate_max_happiness(self):
        return max(self.calculate_happiness(p) for p in permutations(self.people))


def test_p1():
    d = DinnerTable(open('day13test.txt').readlines())
    d.parse_lines()
    assert d.calculate_max_happiness() == 330


p1 = DinnerTable(INPUT)
p1.parse_lines()
print("Part 1: ", p1.calculate_max_happiness())

p2 = DinnerTable(INPUT, add_neutral_person=True)
p2.parse_lines()
print("Part 2: ", p2.calculate_max_happiness())

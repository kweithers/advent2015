from typing import List, Iterator
INPUT = open('day16.txt').readlines()


class SueSolver:
    def __init__(self, lines: List[str]):
        self.sues: dict[int, dict[str, int]] = self.parse_lines(lines)

    def parse_lines(self, lines: List[str]) -> dict[int, dict[str, int]]:
        return {i+1: self.parse_line(line) for i, line in enumerate(lines)}

    def parse_line(self, line: str) -> dict[str, int]:
        tokens = line.replace(':', '').replace(',', '').split(' ')
        return {tokens[2]: int(tokens[3]), tokens[4]: int(tokens[5]), tokens[6]: int(tokens[7])}

    def solve(self, output: dict[str, int]) -> Iterator[int]:
        return (index for index, sue in self.sues.items() if all(output[k] == v for k, v in sue.items()))

    def conditional_compare(self, key: str, output_value: int, sue_value: int) -> bool:
        match key:
            case 'cats' | 'trees':
                return output_value < sue_value
            case 'pomeranians' | 'goldfish':
                return output_value > sue_value
        return output_value == sue_value

    def solve2(self, output: dict[str, int]) -> Iterator[int]:
        return (index for index, sue in self.sues.items() if all(self.conditional_compare(k, output[k], v) for k, v in sue.items()))


ss = SueSolver(INPUT)
output = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3,
          'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

print("Part 1: ", next(ss.solve(output)))
print("Part 2: ", next(ss.solve2(output)))

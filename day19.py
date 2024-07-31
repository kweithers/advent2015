from typing import List
from collections import defaultdict, Counter
INPUT = 'ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF'
REPLACEMENTS = open('day19.txt').read().splitlines()
TEST_INPUT = 'HOH'
TEST_INPUT2 = 'HOHOHO'
TEST_REPLACEMENTS = ['H => HO', 'H => OH', 'O => HH']
TEST_REPLACEMENTS2 = ['e => H', 'e => O', 'H => HO', 'H => OH', 'O => HH']


class Molecule:
    def __init__(self, molecule: str, replacements: List[str]) -> None:
        self.mol: str = molecule
        self.replacements: set[(str,
                               str)] = self.parse_replacements(replacements)
        self.new_mols: set[str] = set()
        self.current_steps = 0
        self.fewest_steps = float('inf')

    def parse_replacements(self, lines: List[str]) -> set[(str, str)]:
        s = set()
        for line in lines:
            tokens = line.split(' => ')
            s.add((tokens[0], tokens[1]))
        return s

    def add_new_mols_for_this_replacement(self, old: str, new: str) -> None:
        for i in range(len(self.mol)):
            if self.mol[i:i+len(old)] == old:
                self.new_mols.add(self.mol[:i] + new + self.mol[i+len(old):])

    def solve(self) -> int:
        for k, v in self.replacements:
            self.add_new_mols_for_this_replacement(k, v)
        return len(self.new_mols)


def test1():
    m = Molecule(TEST_INPUT, TEST_REPLACEMENTS)
    assert m.solve() == 4

    m = Molecule(TEST_INPUT2, TEST_REPLACEMENTS)
    assert m.solve() == 7


m = Molecule(INPUT, REPLACEMENTS)
print("Part 1: ", m.solve())
print("Part 2: ", sum(1 for c in m.mol if c.isupper()
                      ) - m.mol.count('Rn') - m.mol.count('Ar') - 2 * m.mol.count('Y') - 1)

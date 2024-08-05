from dataclasses import dataclass
from typing import Optional
import pytest
INPUT = open('day23.txt').read().splitlines()


@dataclass(frozen=True)
class Instruction:
    i: str
    r: Optional[str]
    offset: Optional[int]


class Computer:

    def __init__(self, lines: list[str], a: int = 0, b: int = 0) -> None:
        self.instructions: list[Instruction] = [
            self.parse_line(line) for line in lines]
        self.a: int = a
        self.b: int = b
        self.pc: int = 0

    def parse_line(self, line: str) -> Instruction:
        tokens = line.split(' ')
        match tokens[0]:
            case 'hlf' | 'tpl' | 'inc':
                return Instruction(tokens[0], tokens[1], None)
            case 'jmp':
                return Instruction(tokens[0], None, int(tokens[1]))
            case 'jie' | 'jio':
                return Instruction(tokens[0], tokens[1], int(tokens[2]))
            case _:
                raise ValueError("Bad instruction")

    def apply_instruction(self, inst: Instruction) -> None:
        match inst.i:
            case 'hlf':
                if inst.r == 'a':
                    self.a /= 2
                else:
                    self.b /= 2
                self.pc += 1
            case 'tpl':
                if inst.r == 'a':
                    self.a *= 3
                else:
                    self.b *= 3
                self.pc += 1
            case 'inc':
                if inst.r == 'a':
                    self.a += 1
                else:
                    self.b += 1
                self.pc += 1
            case 'jmp':
                self.pc += inst.offset
            case 'jie':
                if inst.r == 'a' and self.a % 2 == 0:
                    self.pc += inst.offset
                elif inst.r == 'b' and self.b % 2 == 0:
                    self.pc += inst.offset
                else:
                    self.pc += 1
            case 'jio':
                if inst.r == 'a' and self.a == 1:
                    self.pc += inst.offset
                elif inst.r == 'b' and self.b == 1:
                    self.pc += inst.offset
                else:
                    self.pc += 1

    def run(self) -> None:
        while 0 <= self.pc < len(self.instructions):
            self.apply_instruction(self.instructions[self.pc])


def test_bad_instruction():
    with pytest.raises(ValueError):
        TEST_INPUT = ["inc a", "jio a +2", "tpl a", "inc a", "typo"]
        c = Computer(TEST_INPUT)


def test_p1():
    TEST_INPUT = ["inc a", "jio a +2", "tpl a", "inc a"]
    c = Computer(TEST_INPUT)
    c.run()
    assert c.a == 2


c = Computer(INPUT)
c.run()
print("Part 1: ", c.b)

c.a, c.b, c.pc = 1, 0, 0
c.run()
print("Part 2: ", c.b)

from dataclasses import dataclass
from functools import lru_cache
INPUT = open("day07.txt").readlines()


@dataclass
class Instruction:
    inst: str
    direct_amount: int = 0
    source: str = ""
    first: str = ""
    second: str = ""
    shift_amount: int = 0
    target: str = ""


def parse_instruction(line: str):
    parts = line.strip("\n").split(' ')
    if "NOT" in parts:
        return Instruction(inst="NOT", source=parts[1], target=parts[3])
    elif "AND" in parts:
        return Instruction(inst="AND", first=parts[0], second=parts[2], target=parts[4])
    elif "OR" in parts:
        return Instruction(inst="OR", first=parts[0], second=parts[2], target=parts[4])
    elif "LSHIFT" in parts:
        return Instruction(inst=parts[1], source=parts[0], shift_amount=int(parts[2]), target=parts[4])
    elif "RSHIFT" in parts:
        return Instruction(inst=parts[1], source=parts[0], shift_amount=int(parts[2]), target=parts[4])
    else:
        return Instruction(inst="DIRECT", source=parts[0], target=parts[2])


class Circuit:
    def __init__(self):
        self.signals = {}
        self.instructions = {}

    def set_instruction(self, i: Instruction):
        self.instructions[i.target] = i
        if i.inst == "DIRECT" and i.source.isdigit():
            self.signals[i.target] = int(i.source)

    @lru_cache
    def find_signal(self, target: str):
        if target in self.signals:
            return self.signals[target]
        else:
            i = self.instructions[target]
            match i.inst:
                case "DIRECT":
                    return self.find_signal(i.source)
                case "NOT":
                    return ~self.find_signal(i.source) & 0xffff
                case "AND":
                    if i.first.isdigit():
                        return int(
                            i.first) & self.find_signal(i.second)
                    else:
                        return self.find_signal(i.first) & self.find_signal(i.second)
                case "OR":
                    return self.find_signal(i.first) | self.find_signal(i.second)
                case "LSHIFT":
                    return self.find_signal(i.source) << i.shift_amount
                case "RSHIFT":
                    return self.find_signal(i.source) >> i.shift_amount


def part1() -> int:
    c = Circuit()

    for line in INPUT:
        c.set_instruction(parse_instruction(line))

    return c.find_signal('a')


print("Part 1:", part1())

# NOTE: just set the value of b in the input file to 956, the part 1 answer
print("Part 2:", part1())

from typing import List
from collections import defaultdict
INPUT = open("day05.txt").readlines()


def three_vowels(line: str) -> bool:
    n = 0
    for c in line:
        match c:
            case 'a' | 'e' | 'i' | 'o' | 'u':
                n += 1
    return n >= 3


def double_letter(line: str) -> bool:
    current_letter = line[0]
    for i in range(1, len(line)):
        if current_letter == line[i]:
            return True
        current_letter = line[i]
    return False


def no_bad_strings(line: str) -> bool:
    for i in range(0, len(line)-2):
        match line[i:i+2]:
            case 'ab' | 'cd' | 'pq' | 'xy':
                return False
    return True


def is_nice(line: str) -> bool:
    return three_vowels(line) and double_letter(line) and no_bad_strings(line)


def part1(lines: List[str]) -> int:
    return sum((is_nice(x) for x in lines))


def test_part1():
    assert is_nice("ugknbfddgicrmopn")
    assert is_nice("aaa")
    assert not is_nice("jchzalrnumimnmhp")
    assert not is_nice("haegwjzuvuyypxyu")
    assert not is_nice("dvszwmarrgswjxmb")


print("Part 1:", part1(INPUT))


def two_letter_pair(line: str) -> bool:
    s = defaultdict(set)
    s[line[0:2]].add(0)
    for i in range(1, len(line)-1):
        if len([b for b in s[line[i:i+2]] if b != i-1]) > 0:
            return True
        s[line[i:i+2]].add(i)
    return False


def bookcase(line: str) -> bool:
    for i in range(0, len(line)-2):
        if line[i] == line[i+2]:
            return True
    return False


def is_nice2(line: str) -> bool:
    return two_letter_pair(line) and bookcase(line)


def test_part2():
    assert is_nice2("qjhvhtzxzqqjkmpb")
    assert is_nice2("xxyxx")
    assert not is_nice2("uurcxstgmygtbstg")
    assert not is_nice2("ieodomkazucvgmuy")


def part2(lines: List[str]) -> int:
    return sum((is_nice2(x) for x in lines))


print("Part 2:", part2(INPUT))

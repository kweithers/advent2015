import hashlib
INPUT = "bgvyzdsv"


def part1(puzzle_input: str) -> str:
    n = 0
    while True:
        s = puzzle_input + str(n)
        if hashlib.md5(s.encode('utf-8')).hexdigest()[0:5] == "00000":
            return n
        n += 1


def part2(puzzle_input: str) -> str:
    n = 0
    while True:
        s = puzzle_input + str(n)
        if hashlib.md5(s.encode('utf-8')).hexdigest()[0:6] == "000000":
            return n
        n += 1


def test_part1():
    assert part1("abcdef") == 609043
    assert part1("pqrstuv") == 1048970


print("Part 1:", part1(INPUT))
print("Part 2:", part2(INPUT))

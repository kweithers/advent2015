ROW = 3010
COLUMN = 3019
START = 20151125
MULTIPLIER = 252533
DIVISOR = 33554393


def next_number(code: int) -> int:
    return code * MULTIPLIER % DIVISOR


def test_next():
    assert next_number(START) == 31916031


def get_count(row: int, column: int) -> int:
    return sum(range(row+column-1)) + column


current_code = START
for i in range(get_count(ROW, COLUMN) - 1):
    current_code = next_number(current_code)
print("Part 1: ", current_code)

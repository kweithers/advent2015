INPUT = "3113322113"


def solve(s: str) -> int:
    new_string = ""
    current_num = s[0]
    current_count = 1
    for i in range(1, len(s)):
        if s[i] == current_num:
            current_count += 1
        else:
            new_string += str(current_count)
            new_string += current_num
            current_num = s[i]
            current_count = 1

    new_string += str(current_count)
    new_string += current_num

    return new_string


def test_part1():
    assert solve("1") == "11"
    assert solve("11") == "21"
    assert solve("21") == "1211"
    assert solve("1211") == "111221"
    assert solve("111221") == "312211"


s = INPUT
for i in range(50):
    s = solve(s)
    match i:
        case 39:
            print("Part 1:", len(s))
        case 49:
            print("Part 2:", len(s))

INPUT = open("day08.txt").readlines()

code_chars = 0
mem_chars = 0
for line in INPUT:
    l = line.rstrip("\n")
    code_chars += len(l)
    i = 1
    while i <= len(l) - 2:
        match l[i], l[i+1]:
            case "\\", "\\":  # \\
                i += 2
            case "\\", "\"":  # \"
                i += 2
            case "\\", "x":  # \xdd
                i += 4
            case _:
                i += 1
        mem_chars += 1


print("Part 1:", code_chars - mem_chars)

encoded_chars = 0
for line in INPUT:
    l = line.rstrip("\n")
    for i, c in enumerate(l):
        match c:
            case "\"":
                encoded_chars += 2
            case "\\":
                encoded_chars += 2
            case _:
                encoded_chars += 1
    encoded_chars += 2  # for outer quotes


print("Part 2:", encoded_chars - code_chars)

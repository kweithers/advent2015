from itertools import combinations
INPUT = [7, 10, 11, 18, 18, 21, 22, 24, 26,
         32, 36, 40, 40, 42, 43, 44, 46, 47, 49, 50]
LITERS = 150

print("Part 1: ", sum((1 for n in range(1, len(INPUT)+1) for c in combinations(INPUT, n)
                       if sum(c) == LITERS)))

g = [n for n in range(1, len(INPUT)+1) for c in combinations(INPUT, n)
     if sum(c) == LITERS]
print("Part 2: ", g.count(min(g)))

from functools import reduce
INPUT = 34000000


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def filter_factors(l, n):
    return set(f for f in l if f*50 >= n)


i = 1
while True:
    f = factors(i)
    if 10*sum(f) >= INPUT:
        print("Part 1: ", i)
    if 11*sum(filter_factors(f, i)) >= INPUT:
        print("Part 2: ", i)
        break
    i += 1

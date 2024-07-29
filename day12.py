import json
INPUT = open('day12.json').read()


class SantaJSON:

    def __init__(self, j: str, ignore_red: bool = False):
        self.json = json.loads(j)
        self.sum = 0
        self.ignore_red = ignore_red

    def sum_numbers(self, item):
        if isinstance(item, dict):
            self.sum_numbers_dict(item)
        for it in item:
            if isinstance(it, int):
                self.sum += it
            elif isinstance(it, dict):
                self.sum_numbers_dict(it)
            elif isinstance(it, list):
                self.sum_numbers(it)

    def sum_numbers_dict(self, item: dict):
        if "red" in item.values() and self.ignore_red:
            return
        for v in item.values():
            if isinstance(v, int):
                self.sum += v
            elif isinstance(v, dict):
                self.sum_numbers_dict(v)
            elif isinstance(v, list):
                self.sum_numbers(v)


def test_p1():
    s = SantaJSON('[1,2,3]')
    s.sum_numbers(s.json)
    assert s.sum == 6

    s = SantaJSON('{"a":2,"b":4}')
    s.sum_numbers(s.json)
    assert s.sum == 6

    s = SantaJSON('[[[3]]]')
    s.sum_numbers(s.json)
    assert s.sum == 3

    s = SantaJSON('{"a":{"b":4},"c":-1}')
    s.sum_numbers(s.json)
    assert s.sum == 3

    s = SantaJSON('{"a":[-1,1]}')
    s.sum_numbers(s.json)
    assert s.sum == 0

    s = SantaJSON('[-1,{"a":1}]')
    s.sum_numbers(s.json)
    assert s.sum == 0

    s = SantaJSON('[]')
    s.sum_numbers(s.json)
    assert s.sum == 0

    s = SantaJSON('{}')
    s.sum_numbers(s.json)
    assert s.sum == 0


def test_p2():
    s = SantaJSON('[1,2,3]', ignore_red=True)
    s.sum_numbers(s.json)
    assert s.sum == 6

    s = SantaJSON('[1,{"c":"red","b":2},3]', ignore_red=True)
    s.sum_numbers(s.json)
    assert s.sum == 4

    s = SantaJSON('{"d":"red","e":[1,2,3,4],"f":5}', ignore_red=True)
    s.sum_numbers(s.json)
    assert s.sum == 0

    s = SantaJSON('[1,"red",5]', ignore_red=True)
    s.sum_numbers(s.json)
    assert s.sum == 6


s1 = SantaJSON(INPUT)
s1.sum_numbers(s1.json)
print("Part 1: ", s1.sum)

s2 = SantaJSON(INPUT, ignore_red=True)
s2.sum_numbers(s2.json)
print("Part 2: ", s2.sum)

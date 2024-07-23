from collections import defaultdict
INPUT = open("day06.txt").readlines()


def parse_line(line: str):
    parts = line.split(' ')
    instruction = parts[0]
    x0 = int(parts[1].split(',')[0])
    y0 = int(parts[1].split(',')[1])
    x1 = int(parts[3].split(',')[0])
    y1 = int(parts[3].split(',')[1])
    return (instruction, x0, y0, x1, y1)


class Grid:
    def __init__(self):
        self.grid = defaultdict(lambda: False)

    def toggle(self, y0, x0, y1, x1):
        for j in range(y0, y1+1):
            for i in range(x0, x1+1):
                self.grid[(j, i)] = not self.grid[(j, i)]

    def turn_off(self, y0, x0, y1, x1):
        for j in range(y0, y1+1):
            for i in range(x0, x1+1):
                self.grid[(j, i)] = False

    def turn_on(self, y0, x0, y1, x1):
        for j in range(y0, y1+1):
            for i in range(x0, x1+1):
                self.grid[(j, i)] = True

    def apply(self, inst, x0, y0, x1, y1):
        match inst:
            case "toggle":
                self.toggle(y0, x0, y1, x1)
            case "on":
                self.turn_on(y0, x0, y1, x1)
            case "off":
                self.turn_off(y0, x0, y1, x1)

    def lights_on(self) -> int:
        return sum(self.grid.values())


def part1() -> int:
    grid = Grid()

    for line in INPUT:
        inst, x0, y0, x1, y1 = parse_line(line)
        grid.apply(inst, x0, y0, x1, y1)
    return grid.lights_on()


print("Part 1:", part1())


class BrightnessGrid:
    def __init__(self):
        self.grid = defaultdict(lambda: 0)

    def toggle(self, y0, x0, y1, x1):
        for j in range(y0, y1+1):
            for i in range(x0, x1+1):
                self.grid[(j, i)] += 2

    def turn_off(self, y0, x0, y1, x1):
        for j in range(y0, y1+1):
            for i in range(x0, x1+1):
                self.grid[(j, i)] = max(self.grid[(j, i)] - 1, 0)

    def turn_on(self, y0, x0, y1, x1):
        for j in range(y0, y1+1):
            for i in range(x0, x1+1):
                self.grid[(j, i)] += 1

    def apply(self, inst, x0, y0, x1, y1):
        match inst:
            case "toggle":
                self.toggle(y0, x0, y1, x1)
            case "on":
                self.turn_on(y0, x0, y1, x1)
            case "off":
                self.turn_off(y0, x0, y1, x1)

    def lights_on(self) -> int:
        return sum(self.grid.values())


def part2() -> int:
    grid = BrightnessGrid()

    for line in INPUT:
        inst, x0, y0, x1, y1 = parse_line(line)
        grid.apply(inst, x0, y0, x1, y1)
    return grid.lights_on()


print("Part 2:", part2())

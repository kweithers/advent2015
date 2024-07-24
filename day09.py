from collections import defaultdict
from dataclasses import dataclass
INPUT = open("day09.txt").readlines()
TEST = open("day09test.txt").readlines()


@dataclass(frozen=True)
class Edge:
    dest: str
    weight: int


class Graph:
    def __init__(self):
        self.nodes = defaultdict(set)
        self.labels = set()
        self.visited = defaultdict(lambda: False)
        self.min_distance_with_all_nodes = 9999999999999
        self.max_distance_with_all_nodes = -1
        self.current_distance = 0

    def parse_nodes(self, lines):
        for line in lines:
            source, dest, weight = line.split(',')
            self.nodes[source].add(Edge(dest, int(weight)))
            self.nodes[dest].add(Edge(source, int(weight)))
            self.labels.add(source)
            self.labels.add(dest)
            self.visited[source] = False
            self.visited[dest] = False

    def dfs(self, source):
        self.visited[source] = True
        if all(self.visited.values()):
            self.min_distance_with_all_nodes = min(
                self.min_distance_with_all_nodes, self.current_distance)
            self.max_distance_with_all_nodes = max(
                self.max_distance_with_all_nodes, self.current_distance)
        for edge in self.nodes[source]:
            if not self.visited[edge.dest]:
                self.current_distance += edge.weight
                self.dfs(edge.dest)
                self.current_distance -= edge.weight
        self.visited[source] = False


def solve(lines):
    g = Graph()
    g.parse_nodes(lines)
    for source in g.labels:
        g.dfs(source)
    return (g.min_distance_with_all_nodes, g.max_distance_with_all_nodes)


def test_solve():
    assert solve(TEST) == (605, 982)


p1, p2 = solve(INPUT)
print("Part 1:", p1)
print("Part 2:", p2)

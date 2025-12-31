from helpers import execute
from ds import UnionFind
import math
import itertools as it
import heapq
from collections import Counter

filename = "inputs/input08.txt"
with open(filename) as f:
    lines = f.read().splitlines()

circuits = [
    (i, list(map(int, line.split(','))))
    for i, line in enumerate(lines)
]
n = len(circuits)


def build_distance_heap(circuits):
    heap = [
        (math.dist(c1[1], c2[1]), c1[0], c2[0])
        for c1, c2 in it.combinations(circuits, 2)
    ]
    heapq.heapify(heap)
    return heap


def part1():
    ufd = UnionFind(n)
    heap = build_distance_heap(circuits)

    for _, i, j in heapq.nsmallest(1000, heap):
        ufd.unite(i, j)

    cluster_sizes = Counter(ufd.find(i) for i in range(n))
    return math.prod(size for _, size in cluster_sizes.most_common(3))


def part2():
    ufd = UnionFind(n)
    heap = build_distance_heap(circuits)

    while ufd.count > 1:
        _, i, j = heapq.heappop(heap)
        ufd.unite(i, j)
        if ufd.count == 1:
            return circuits[i][1][0] * circuits[j][1][0]


execute(part1)
execute(part2)

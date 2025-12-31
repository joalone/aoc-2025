from helpers import execute
import math
import itertools as it

filename = "inputs/input09.txt"
with open(filename) as f:
    lines = f.read().splitlines()

points = [list(map(int, line.split(','))) for line in lines]


def hypervolume(p, q):
    return math.prod(abs(x-y)+1 for x, y in zip(p, q))


def squares_intersect(p1, p2, q1, q2):
    x1, x2 = sorted([p1[0], p2[0]])
    y1, y2 = sorted([p1[1], p2[1]])
    X1, X2 = sorted([q1[0], q2[0]])
    Y1, Y2 = sorted([q1[1], q2[1]])
    return x1 < X2 and X1 < x2 and y1 < Y2 and Y1 < y2


def part1():
    return max(
        hypervolume(p, q)
        for p, q in it.combinations(points, 2)
    )


def part2():
    # Idea of sorting thanks to @4HbQ
    pairs = sorted(it.combinations(points, 2),
                   key=lambda p: hypervolume(*p), reverse=True)
    lines = sorted(it.pairwise(points + [points[0]]),
                   key=lambda p: hypervolume(*p), reverse=True)

    for p1, p2 in pairs:
        if all(not squares_intersect(p1, p2, q1, q2) for q1, q2 in lines):
            return hypervolume(p1, p2)
    return 0


execute(part1)
execute(part2)

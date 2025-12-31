from helpers import execute
from bisect import bisect_right

filename = "inputs/input05.txt"
with open(filename) as f:
    lines_intervals, lines_numbers = [
        lines.splitlines()
        for lines in f.read().split("\n\n")
    ]

intervals = [list(map(int, r.split('-'))) for r in lines_intervals]
numbers = [int(x) for x in lines_numbers]


def sort_and_merge_intervals(intervals):
    result = []
    for a, b in sorted(intervals):
        if not result:
            result.append((a, b))
            continue
        x, y = result[-1]
        if y < a:
            result.append((a, b))
        else:
            result[-1] = (x, max(y, b))
    return result


def is_covered(x, left_ends, right_ends):
    i = bisect_right(left_ends, x) - 1
    return i >= 0 and x <= right_ends[i]


def part1():
    left_ends, right_ends = list(zip(*sort_and_merge_intervals(intervals)))
    return sum(is_covered(x, left_ends, right_ends) for x in numbers)


def part2():
    return sum(b-a+1 for a, b in sort_and_merge_intervals(intervals))


execute(part1)
execute(part2)

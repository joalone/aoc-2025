from helpers import execute

filename = "inputs/input03.txt"
with open(filename) as f:
    lines = f.read().splitlines()


def maximum_joltage(line, k):
    n = len(line)
    i = 0
    result = []
    for j in reversed(range(k)):
        window = line[i:n-j]
        i += window.index(max(window))
        result.append(line[i])
        i += 1
    return int(''.join(result))


def part1():
    return sum(maximum_joltage(x, 2) for x in lines)


def part2():
    return sum(maximum_joltage(x, 12) for x in lines)


execute(part1)
execute(part2)

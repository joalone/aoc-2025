from helpers import execute

filename = "inputs/input01.txt"
with open(filename) as f:
    lines = f.read().splitlines()

signs = {'L': -1, 'R': +1}
steps = [signs[line[0]] * int(line[1:]) for line in lines]


def count_landings(start, mod):
    x = start
    result = 0
    for y in steps:
        x = (x + y) % mod
        result += x == 0
    return result


def count_passes(start, mod):
    x = start
    result = 0
    for y in steps:
        s = x + y
        if y > 0:
            result += s // mod
        else:
            result -= (s - 1) // mod
            result -= x == 0
        x = s % mod
    return result


def part1():
    return count_landings(50, 100)


def part2():
    return count_passes(50, 100)


execute(part1)
execute(part2)

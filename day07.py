from helpers import execute

filename = "inputs/input07.txt"
with open(filename) as f:
    lines = f.read().splitlines()


def count_splits():
    memo = [x == 'S' for x in lines[0]]
    result = 0
    for line in lines[1:]:
        for i, x in enumerate(line):
            if x == '^' and memo[i] == 1:
                memo[i-1], memo[i], memo[i+1] = 1, 0, 1
                result += 1
    return result


def count_paths():
    memo = [x == 'S' for x in lines[0]]
    for line in lines[1:]:
        for i, x in enumerate(line):
            if x == '^':
                memo[i-1] += memo[i]
                memo[i+1] += memo[i]
                memo[i] = 0
    return memo


def part1():
    return count_splits()


def part2():
    return sum(count_paths())


execute(part1)
execute(part2)

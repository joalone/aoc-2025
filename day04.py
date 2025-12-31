from helpers import execute

dirs = [[x, y] for x in [-1, 0, 1] for y in [-1, 0, 1] if x != 0 or y != 0]

filename = "inputs/input04.txt"
with open(filename) as f:
    lines = f.read().splitlines()

grid = [list(line) for line in lines]
m, n = len(grid), len(grid[0])


def within_bounds(i, j):
    return 0 <= i < m and 0 <= j < n


def count_adjacent(i, j):
    return sum(within_bounds(i + di, j + dj) and grid[i + di][j + dj] == '@' for di, dj in dirs)


def is_valid(i, j):
    return within_bounds(i, j) and grid[i][j] == '@' and count_adjacent(i, j) < 4


def flood_fill(i, j):
    if not is_valid(i, j):
        return 0
    grid[i][j] = '.'
    return 1 + sum(flood_fill(i + di, j + dj) for di, dj in dirs)


def part1():
    return sum(is_valid(i, j) for i in range(m) for j in range(n))


def part2():
    return sum(flood_fill(i, j) for i in range(m) for j in range(n))


execute(part1)
execute(part2)

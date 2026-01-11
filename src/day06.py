from helpers import execute
import math

filename = "inputs/input06.txt"
with open(filename) as f:
    *lines, line_operations = f.read().splitlines()

operations = line_operations.split()


def compute(operands, operations):
    return sum(
        sum(map(int, col)) if op == '+' else math.prod(map(int, col))
        for col, op in zip(operands, operations)
    )


def part1():
    rows = map(str.split, lines)
    operands = list(map(list, zip(*rows)))
    return compute(operands, operations)


def part2():
    operands = []
    operand = []
    cols = map(''.join, zip(*lines))
    for line in cols:
        if line.strip():
            operand.append(line)
        else:
            operands.append(operand)
            operand = []
    if operand:
        operands.append(operand)
    return compute(operands, operations)


execute(part1)
execute(part2)

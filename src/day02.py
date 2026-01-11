from helpers import execute
from sympy import mobius

pow10 = [pow(10, i) for i in range(32)]

filename = "inputs/input02.txt"
with open(filename) as f:
    lines = f.read().split(",")

intervals = [list(map(int, line.split("-"))) for line in lines]


def arithmetic_sum(a, d, n):
    lo, hi = a, a + (n - 1) * d
    return n * (lo + hi) // 2


def repeat_multiplier(block_len, reps):
    return (pow10[block_len * reps] - 1) // (pow10[block_len] - 1)


def floor_div(a, q):
    return a // q


def ceil_div(a, q):
    return (a + q - 1) // q


def sum_pattern_matches(lo, hi, digits, reps):
    block_len = digits // reps
    pattern = repeat_multiplier(block_len, reps)
    block_min = max(pow10[block_len - 1], ceil_div(lo, pattern))
    block_max = min(pow10[block_len] - 1, floor_div(hi, pattern))
    
    if block_min > block_max:
        return 0
    return arithmetic_sum(block_min * pattern, pattern, block_max - block_min + 1)


def sum_even_invalid(lo, hi):
    digits_lo, digits_hi = len(str(lo)), len(str(hi))
    return sum(
        sum_pattern_matches(lo, hi, digits, 2)
        for digits in range(digits_lo, digits_hi + 1)
        if digits % 2 == 0
    )


def sum_all_invalid(lo, hi):
    # Idea of Möbius function thanks to @light_ln2
    digits_lo, digits_hi = len(str(lo)), len(str(hi))
    return sum(
        -mu * sum_pattern_matches(lo, hi, digits, r)
        for digits in range(digits_lo, digits_hi + 1)
        for r in range(2, digits + 1)
        if digits % r == 0 and (mu := mobius(r)) != 0
    )


def part1():
    return sum(sum_even_invalid(lo, hi) for lo, hi in intervals)


def part2():
    return sum(sum_all_invalid(lo, hi) for lo, hi in intervals)


execute(part1)
execute(part2)

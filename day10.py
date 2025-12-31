from helpers import execute
from collections import deque
from scipy.optimize import linprog

filename = "inputs/input10.txt"
with open(filename) as f:
    lines = f.read().splitlines()


def light_to_bitmask(light):
    return sum(1 << i for i, x in enumerate(light) if x == '#')


def wiring_to_bitmask(wiring):
    return sum(1 << x for x in wiring)


machines = []
for line in lines:
    light_str, *wirings_lines, joltage_str = line.split()
    light_mask = light_to_bitmask(light_str[1:-1])
    wirings_mask = [
        wiring_to_bitmask(list(map(int, w[1:-1].split(','))))
        for w in wirings_lines
    ]
    joltage = list(map(int, joltage_str[1:-1].split(',')))
    machines.append([light_mask, wirings_mask, joltage])


def min_steps_light(light, wirings):
    if light == 0:
        return 0
    queue = deque((1, w) for w in wirings)
    visited = set()
    while queue:
        i, state = queue.popleft()
        if state == light:
            return i
        if state not in visited:
            queue.extend((i + 1, state ^ w) for w in wirings)
            visited.add(state)
    return None


def min_steps_joltage(joltage, wirings):
    c = [1] * len(wirings)
    A = [[(w >> i) & 1 for w in wirings] for i in range(len(joltage))]
    b = joltage
    result = linprog(c, A_eq=A, b_eq=b, integrality=1)
    if not result.success:
        return None
    return int(result.fun)


def part1():
    return sum(steps
               for light, wirings, _ in machines
               if (steps := min_steps_light(light, wirings)) != None
               )


def part2():
    return sum(steps
               for _, wirings, joltage in machines
               if (steps := min_steps_joltage(joltage, wirings)) != None
               )


execute(part1)
execute(part2)

from helpers import execute
from functools import cache

filename = "inputs/input11.txt"
with open(filename) as f:
    lines = f.read().splitlines()

graph = {
    k: v.split()
    for k, v in (line.split(":", 1) for line in lines)
} | {"out": []}


@cache
def count_paths(src, dst):
    if src == dst:
        return 1
    return sum(count_paths(w, dst) for w in graph[src])


def part1():
    return count_paths("you", "out")


def part2():
    # Assumes no cycle including "dac" or "fft"
    return (count_paths("svr", "fft")  # If "dac" comes before "fft"
            * count_paths("fft", "dac")
            * count_paths("dac", "out")
            + count_paths("svr", "dac")  # If "dac" precedes "fft"
            * count_paths("dac", "fft")
            * count_paths("fft", "out"))


execute(part1)
execute(part2)

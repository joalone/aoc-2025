from helpers import execute

filename = "inputs/input12.txt"
with open(filename) as f:
    lines = f.read().splitlines()

shapes = []
tasks = []
shape = []
for line in lines:
    line = line.strip()
    if not line:
        continue

    if "x" in line:
        pair, nums = line.split(":")
        w, h = map(int, pair.split("x"))
        counts = list(map(int, nums.split()))
        tasks.append(((h, w), counts))
        continue

    if line.endswith(":") and shape:
        shapes.append(shape)
        shape = []
        continue

    if all(c in "#." for c in line):
        shape.append(line)

if shape:
    shapes.append(shape)


def get_shape(shape_lines):
    m, n = len(shape_lines), len(shape_lines[0])
    return [(i, j) for i in range(m) for j in range(n) if shape_lines[i][j] == '#']


def normalize(shape):
    min_i, min_j = map(min, zip(*shape))
    return tuple(sorted((i - min_i, j - min_j) for i, j in shape))


def rotate(shape):
    return normalize([(j, -i) for i, j in shape])


def flip(shape):
    return normalize([(i, -j) for i, j in shape])


def all_orientations(shape):
    seen = set()
    result = []
    current = shape
    for _ in range(4):
        current = rotate(current)
        for variant in (current, flip(current)):
            if variant not in seen:
                seen.add(variant)
                result.append(variant)
    return result


orientations = [all_orientations(get_shape(shape)) for shape in shapes]


def fits(board, cells, i0, j0):
    m, n = len(board), len(board[0])
    for di, dj in cells:
        i, j = i0 + di, j0 + dj
        if not (0 <= i < m and 0 <= j < n) or board[i][j]:
            return False
    return True


def place(board, cells, i0, j0, value):
    for di, dj in cells:
        i, j = i0 + di, j0 + dj
        board[i][j] = value


def backtrack(board, counts):
    if all(c == 0 for c in counts):
        return True

    m, n = len(board), len(board[0])
    s = min(
        (i for i, c in enumerate(counts) if c > 0),
        key=lambda i: len(orientations[i])
    )
    for orientation in orientations[s]:
        for i in range(m):
            for j in range(n):
                if fits(board, orientation, i, j):
                    place(board, orientation, i, j, True)
                    counts[s] -= 1

                    if backtrack(board, counts):
                        return True

                    counts[s] += 1
                    place(board, orientation, i, j, False)
    return False


def can_fit(counts, dims):
    m, n = dims
    board = [[False] * n for _ in range(m)]
    shapes_area = sum(c * len(o[0]) for c, o in zip(counts, orientations))
    board_area = m * n
    if shapes_area > board_area:
        return False
    return backtrack(board, counts.copy())


def part1():
    return sum(
        can_fit(counts, dims)
        for dims, counts in tasks
    )


execute(part1)

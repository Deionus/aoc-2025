from utils import ADJ_8, default_grid
from runner import go


def process(input):
    return [list(line) for line in input.split("\n")]


def part1(input):
    grid = default_grid(input, lambda: ".")
    return sum([sum([1 for a, b in ADJ_8 if grid[(a+row, b+col)] == "@"]) < 4 for (row, col), val in list(grid.items()) if val == "@"])


def part2(input):
    grid = input
    total = 0
    N = len(grid)
    M = len(grid[0])

    removed = 0
    while True:
        for row in range(N):
            for col in range(M):
                if grid[row][col] == ".": continue
                r = sum([1 for x, y in ((row+a, col+b) for a,b in ADJ_8) if x >= 0 and x < N and y >= 0 and y < M and grid[x][y] == "@"]) < 4
                removed += r
                total += r
                if r: grid[row][col] = "."
        
        if not removed: break
        removed = 0

    return total


go(process, part1, part2)
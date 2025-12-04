from utils import g

ADJACENT = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0,1), (1,-1), (1,0), (1,1))

def part1():
    grid = g()
    total = 0
    N = len(grid)
    M = len(grid[0])
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == ".": continue

            c = 0
            for a, b in ADJACENT:
                x = row+a
                y = col+b
                if x < 0 or x >= N or y < 0 or y >= M: continue
                if grid[x][y] == "@":
                    c += 1
            
            if c < 4:
                print(row, col)
                total += 1
            
    return total


def part2():
    grid = g()
    total = 0
    N = len(grid)
    M = len(grid[0])

    removed = []
    while True:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == ".": continue

                c = 0
                for a, b in ADJACENT:
                    x = row+a
                    y = col+b
                    if x < 0 or x >= N or y < 0 or y >= M: continue
                    if grid[x][y] == "@":
                        c += 1
                
                if c < 4:
                    print(row, col)
                    removed.append((row,col))
        
        if removed:
            total += len(removed)
            for r in removed:
                grid[r[0]][r[1]] = "."
        else:
            break

        removed = []

    return total


print(part1())
print(part2())
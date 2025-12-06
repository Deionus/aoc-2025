import sys, collections


ADJ_8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0,1), (1,-1), (1,0), (1,1))
ADJ_4 = ((-1, 0), (1, 0), (0, -1), (0, 1))

def o():
    text = open(f"inputs/{sys.argv[0][:-3]}.txt", "r").read()
    return text


def l():
    return o().split("\n")


def c():
    return o().split(",")


def default_grid(grid, default):
    """
    Turns a 2d array 'grid' into a default dict. `default` is a lambda
    grid: [[1, 2, 3, 4], [3, 4, 5, 6]]
    """
    return collections.defaultdict(default, {(i,j): grid[i][j] for i in range(len(grid)) for j in range(len(grid[0]))})
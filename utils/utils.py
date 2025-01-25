

def is_index_valid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def parse_grid():
    with (open('input.txt') as f):
        grid = [[c for c in l[:-1]] for l in f.readlines()]
        return grid
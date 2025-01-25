
from utils.utils import is_index_valid, parse_grid


def calculate_trailheads_score(grid):
    n, m = len(grid), len(grid[0])
    starts = find_starting_points(grid)
    queue = [(i,j,0, (i,j)) for i,j in starts]
    score = {s: 0 for s in starts}
    directions = [[1,0], [0,1], [-1, 0], [0,-1]]

    while queue:
        ci, cj, v, start = queue.pop()

        if v == 9:
            score[start] += 1
            continue

        for di, dj in directions:
            ni, nj = ci + di, cj + dj
            if is_index_valid(ni, nj, n, m) and int(grid[ni][nj]) - int(v) == 1:
                queue.append((ni, nj, v+1, start))
    return sum(nines for nines in score.values())


def find_starting_points(grid):
    starts = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "0":
                starts.append((i,j))
    return starts

def main():
    grid = parse_grid()
    print(calculate_trailheads_score(grid))


if __name__ == '__main__':
    main()
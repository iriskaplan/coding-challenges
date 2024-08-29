# write a naive solution and then improve it
from collections import deque


def find_sum_galaxies_length():
    with open("input.txt", "r") as input_file:
        grid = [list(line.strip()) for line in input_file.readlines()]
        sum_length = 0
        expended_grid = expend_grid(grid)
        updated_grid, galaxies = find_galaxies(expended_grid)

        for i, galaxy in enumerate(galaxies):
            dist_mat = find_dists_in_grid(grid, galaxies[i])
            for j in range(i + 1, len(galaxies)):
                k, l = galaxies[j]
                sum_length += dist_mat[k][l]
        return sum_length
        # print_mat(dist_mat)
        #     print(dist_mat)


def find_dists_in_grid(grid, start):
    dist_mat = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    n, m = len(grid), len(grid[0])
    si, sj = start
    dist_mat[si][sj] = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([start])

    while queue:
        i, j = queue.popleft()

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if is_valid_index(n, m, ni, nj) and dist_mat[ni][nj] == -1:  # not visited
                dist_mat[ni][nj] = 1 + dist_mat[i][j]
                queue.append((ni, nj))
    return dist_mat


def print_mat(mat):
    for line in mat:
        print(''.join(str(line)))


def is_valid_index(n, m, i, j):
    return 0 <= i < n and 0 <= j < m


def expend_grid(grid):
    expended_rows, expended_cols = {x for x in range(len(grid))}, {x for x in range(len(grid[0]))}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "#":

                if i in expended_rows:
                    expended_rows.remove(i)
                if j in expended_cols:
                    expended_cols.remove(j)

    for i, idx in enumerate(expended_rows):
        grid.insert(i + idx, ['.' for _ in range(len(grid[0]))])

    for i, idx in enumerate(expended_cols):
        for row in grid:
            row.insert(i + idx, '.')

    return grid


def find_galaxies(grid):
    galaxies = []
    galaxies_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "#":
                galaxies_count += 1
                grid[i][j] = galaxies_count
                galaxies.append((i, j))
    return grid, galaxies


print(find_sum_galaxies_length())

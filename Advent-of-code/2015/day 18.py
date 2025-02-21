
from utils.utils import is_index_valid, parse_grid, get_8_dirs


def calculate_next_value(i, j, grid):
    n, m = len(grid), len(grid[0])
    directions = get_8_dirs()
    lights_count = 0
    for di, dj in directions:
         if is_index_valid(i+di, j+dj, n, m) and grid[i+di][j+dj] == "#":
             lights_count += 1

    if grid[i][j] == "#":
        return "#" if 2 <= lights_count <= 3 else "."

    return "#" if lights_count == 3 else "."


def flip_lights(grid):
    n, m = len(grid), len(grid[0])
    corners = [(0, 0), (0, m-1), (n-1, 0), (n-1, m-1)]
    for i, j in corners:
        grid[i][j] = "#"

    next_grid = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(100):
        for i in range(n):
            for j in range(m):
                if (i, j) not in corners:
                    next_grid[i][j] = calculate_next_value(i, j, grid)
                else:
                    next_grid[i][j] = "#"
        grid = next_grid.copy()
        next_grid = [[0 for _ in range(n)] for _ in range(m)]
    return grid

def count_on(grid):
    n, m = len(grid), len(grid[0])
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "#":
                count += 1
    return count

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(''.join(matrix[i]))
    print()

def main():
    grid = parse_grid()
    grid_after_steps = flip_lights(grid)
    print(count_on(grid_after_steps))


if __name__ == '__main__':
    main()
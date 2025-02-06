from utils.utils import is_index_valid, parse_grid, get_4_dirs

def dfs(start, grid):
    n, m = len(grid), len(grid[0])
    directions = get_4_dirs()
    area = 0
    perimeter = 0
    ci, cj = start
    letter = grid[ci][cj]
    visited = [(ci, cj)]
    queue = [(ci, cj)]

    while queue:
        ci, cj = queue.pop()
        area += 1
        for di, dj in directions:
            ni, nj = ci + di, cj + dj
            idx_valid = is_index_valid(ni, nj, n, m)
            if idx_valid and (ni, nj) not in visited and letter == grid[ni][nj]:
                visited.append((ni, nj))
                queue.append((ni, nj))
            elif (idx_valid and letter != grid[ni][nj]) or (not idx_valid):
                perimeter += 1
    visited.remove(start)
    return area, perimeter, visited


def main():
    grid = parse_grid()
    n, m = len(grid), len(grid[0])
    queue = [(i, j) for i in range(n) for j in range(m)]

    price = 0

    while queue:
        start = queue.pop()
        c_area, c_per, c_visited = dfs(start, grid)
        c_price = c_area * c_per
        print(f"For {grid[start[0]][start[1]]} area: {c_area} per: {c_per}")
        price += c_price

        for v in c_visited:
            queue.remove(v)
    print(price)
    return price


if __name__ == '__main__':
    main()
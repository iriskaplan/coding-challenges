from utils.utils import is_index_valid, parse_grid


def dfs(start, grid):
    n, m = len(grid), len(grid[0])
    border_type = {"top": (-1, 0), "bottom": (1, 0), "left": (0, -1), "right": (0, 1)}
    reversed_border_map = {(-1, 0): "top", (1, 0): "bottom", (0, -1): "left", (0, 1): "right"}
    area = 0
    perimeter = 0
    sides = 0
    ci, cj = start
    visited = {(ci, cj): []}
    queue = [(ci, cj)]

    while queue:
        ci, cj = queue.pop()
        letter = grid[ci][cj]
        area += 1
        for k, (di, dj) in border_type.items():
            ni, nj = ci + di, cj + dj
            idx_valid = is_index_valid(ni, nj, n, m)
            if idx_valid and (ni, nj) not in visited and letter == grid[ni][nj]:
                visited[(ni, nj)] = []
                queue.append((ni, nj))
            elif (idx_valid and letter != grid[ni][nj]) or (not idx_valid):
                perimeter += 1
                visited[(ci, cj)].append(reversed_border_map[(di, dj)])

    for k, borders in visited.items():
        ci, cj = k

        for border in borders:
            neighbors_with_border = 0
            if border == "top" or border == "bottom":
                li, lj = ci, cj - 1
                ri, rj = ci, cj + 1

                if (li, lj) in visited and border in visited[(li, lj)]:
                    neighbors_with_border += 1
                if (ri, rj) in visited and border in visited[(ri, rj)]:
                    neighbors_with_border += 1
            else:
                ui, uj = ci - 1, cj
                bi, bj = ci + 1, cj

                if (ui, uj) in visited and border in visited[(ui, uj)]:
                    neighbors_with_border += 1
                if (bi, bj) in visited and border in visited[(bi, bj)]:
                    neighbors_with_border += 1
            if neighbors_with_border == 0:
                sides += 1
            elif neighbors_with_border == 1:
                sides += 0.5


    visited.pop(start)
    return area, sides, visited


def main():
    grid = parse_grid()
    n, m = len(grid), len(grid[0])
    queue = [(i, j) for i in range(n) for j in range(m)]

    price = 0

    while queue:
        start = queue.pop()
        c_area, c_per, c_visited = dfs(start, grid)
        c_price = c_area * c_per

        price += c_price
        print(f"For {grid[start[0]][start[1]]} area: {c_area} per: {c_per}, price: {c_price}")
        for v in c_visited:
            queue.remove(v)
    print(price)
    return price


if __name__ == '__main__':
    main()
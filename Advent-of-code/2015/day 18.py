import numpy as np
import cv2
from utils.utils import is_index_valid, parse_grid, get_8_dirs


def change_grid_to_bin(grid):
    return np.array([[1 if cell == "#" else 0 for cell in row] for row in grid], dtype=np.uint8)

def calculate_next_value(i, j, grid):
    n, m = grid.shape
    directions = get_8_dirs()
    lights_count = sum(grid[i + di, j + dj] for di, dj in directions if is_index_valid(i + di, j + dj, n, m))

    if grid[i, j] == 1:
        return 1 if 2 <= lights_count <= 3 else 0
    return 1 if lights_count == 3 else 0

def simulate_game(grid, steps=100):
    n, m = grid.shape
    corners = [(0, 0), (0, m - 1), (n - 1, 0), (n - 1, m - 1)]

    frames = [grid.copy()]

    for _ in range(steps):
        next_grid = grid.copy()
        for i in range(n):
            for j in range(m):
                if (i, j) not in corners:
                    next_grid[i, j] = calculate_next_value(i, j, grid)
                else:
                    next_grid[i, j] = 1

        grid = next_grid.copy()
        frames.append(grid.copy())

    return frames

grid = change_grid_to_bin(parse_grid())
frames = simulate_game(grid)
for frame in frames:
    img = (frame * 255).astype(np.uint8)
    img_resized = cv2.resize(img, (500, 500), interpolation=cv2.INTER_NEAREST)

    cv2.imshow("Game of Life", img_resized)
    if cv2.waitKey(100) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
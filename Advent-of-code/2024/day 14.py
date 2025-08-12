import numpy as np
from PIL import Image, ImageDraw

def calculate_position(x, y, vx, vy, t, n, m):
    nx = (x + t * vx) % n
    ny = (y + t * vy) % m
    return int(nx), int(ny)

def parse_line(line):
    p, v = line.split(' ')
    p = p[2:].split(',')
    px, py = int(p[0]), int(p[1])
    v = v[2:].split(',')
    vx, vy = int(v[0].strip()), int(v[1].strip())
    return px, py, vx, vy

def main():
    k = 7858 # solution to 103x - 101y = (h_c - v_c)
    n, m = 101, 103

    with open('input.txt') as f:
        lines = f.readlines()

    robots = [parse_line(line) for line in lines]

    frames = []
    arr = np.ones((n, m), dtype=np.uint8) * 255
    for (px, py, vx, vy) in robots:
        tpx, tpy = calculate_position(px, py, vx, vy, k, n, m)
        arr[tpx, tpy] = 0

    img = Image.fromarray(arr, mode="L").convert("RGB")
    draw = ImageDraw.Draw(img)
    draw.text((5, 5), f"Step {k}", fill=(255, 0, 0))

    frames.append(img)

    frames[0].save(
        "robots2.gif",
        save_all=True,
        append_images=frames[1:],
        duration=200,
        loop=0
    )
    print("Saved GIF")

if __name__ == "__main__":
    main()
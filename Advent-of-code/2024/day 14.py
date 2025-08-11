
def calculate_position(x, y, vx, vy, t, n, m):
    nx = (x + t * vx) % n
    ny = (y + t * vy) % m
    return nx, ny


def parse_line(line):
    p, v = line.split(' ')
    p = p[2:].split(',')
    px, py = int(p[0]), int(p[1])
    v = v[2:].split(',')
    vx, vy = int(v[0].strip()), int(v[1].strip())
    return px, py, vx, vy


def init_grid(n,m):
    return [['.' for _ in range(n)] for _ in range(m)]


def print_grid(grid):
    for i in range(len(grid)):
        print(''.join(grid[i]))


def main():
    t = 100
    n, m = 101, 103
    q1, q2, q3, q4 = 0, 0, 0, 0
    with (open('input.txt') as f):
        lines = f.readlines()
        robots = []
        for line in lines:
            px, py, vx, vy = parse_line(line)
            robots.append((px, py, vx, vy))
            
            tpx, tpy = calculate_position(px, py, vx, vy, t, n, m)
            if tpx < (n //2) and tpy < (m // 2):
                q1 += 1
            elif tpx > (n //2) and tpy < (m // 2):
                q2 += 1
            elif tpx < (n // 2) and tpy > (m // 2):
                q3 += 1
            elif tpx > (n // 2) and tpy > (m // 2):
                q4 += 1
        print(q1 * q2 * q3 * q4)

main()
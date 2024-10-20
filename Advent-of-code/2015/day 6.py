
def true(x):
    return True

def false(x):
    return False

def toggle(x):
    return not x


def read_instructions():
    with open('input.txt') as f:
        lines = f.readlines()
        parsed_instructions = []
        for line in lines:
            line_list = line.split()

            if line_list[0] == 'toggle':
                s_c, s_r = [int(n) for n in line_list[1].split(',')]
                e_c, e_r = [int(n) for n in line_list[3].split(',')]
                parsed_instructions.append((line_list[0], (s_r, e_r), (s_c, e_c)))
            else:
                s_c, s_r = [int(n) for n in line_list[2].split(',')]
                e_c, e_r = [int(n) for n in line_list[4].split(',')]
                parsed_instructions.append((line_list[1],(s_r, e_r), (s_c, e_c)))
        return parsed_instructions


def count_lights_on(instructions):
    map_ = {'on': true, 'off': false, 'toggle': toggle}
    lights = 0
    grid = [[False for _ in range(1000)] for _ in range(1000)]
    for instruction, rows, cols in instructions:
        for r in range(rows[0], rows[1] + 1):
            for c in range(cols[0], cols[1] + 1):
                grid[r][c] = map_[instruction](grid[r][c])

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                lights += 1

    return lights


instructions = read_instructions()
print(count_lights_on(instructions))

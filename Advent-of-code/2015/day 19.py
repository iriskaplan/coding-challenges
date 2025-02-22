
def parse_input():
    with open('input.txt') as f:
        lines = f.readlines()
        replace_map = dict()
        s = ''
        for line in lines:
            line_list = line.split()
            if "=>" in line_list:
                replace_map[line_list[2]] = line_list[0]
            elif line:
                s = line
        return s, replace_map

def dfs(start_s, replace_map):
    strings_q = [(start_s, 0)]
    visited = {start_s:0}
    while strings_q:
        s, s_steps = strings_q.pop()

        if s == "e":
            print(s_steps)
        # adjacent strings are strings can get to in one replace
        adj_strings = replace_one_step(replace_map, s)
        for adj_s in adj_strings:
            if adj_s in visited and s_steps + 1 < visited[adj_s]:
                visited[adj_s] = s_steps + 1
            if adj_s not in visited:
                strings_q.append((adj_s, s_steps+1))
                visited[adj_s] = s_steps + 1
    return visited["e"]


def main():
    start_s, replace_map = parse_input()
    steps = dfs(start_s, replace_map)
    print(steps)

def replace_subset(replace_map, strings):
    all_replaced = set()
    for s in strings:
        replaced_strings = replace_one_step(replace_map, s)
        all_replaced = all_replaced.union(replaced_strings)
    return all_replaced

def replace_one_step(replace_map, start_s):
    replaced_strings = set()
    for rule in replace_map:
        start = 0
        indices = []
        while True:
            start = start_s.find(rule, start)
            if start == -1:
                break
            indices.append(start)
            start += len(rule)

        for i in indices:
            new_s = start_s[:i] + replace_map[rule] + start_s[i + len(rule):]
            replaced_strings.add(new_s)
    return replaced_strings


if __name__ == '__main__':
    main()
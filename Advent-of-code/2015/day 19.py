
def parse_input():
    with open('input.txt') as f:
        lines = f.readlines()
        replace_map = dict()
        s = ''
        for line in lines:
            line_list = line.split()
            if "=>" in line_list:
                if line_list[0] not in replace_map:
                    replace_map[line_list[0]] = [line_list[2]]
                else:
                    replace_map[line_list[0]].append(line_list[2])
            elif line:
                s = line
        return s, replace_map

def main():
    start_s, replace_map = parse_input()

    replaced_strings = set()
    for i in range(len(start_s)):
        if start_s[i] in replace_map:
            for rep_s in replace_map[start_s[i]]:
                new_s = start_s[:i] + rep_s + start_s[i+1:]
                replaced_strings.add(new_s)
        if i < (len(start_s) - 1) and start_s[i:i+2] in replace_map:
            for rep_s in replace_map[start_s[i:i+2]]:
                new_s = start_s[:i] + rep_s + start_s[i + 2:]
                replaced_strings.add(new_s)
    print(len(replaced_strings))



if __name__ == '__main__':
    main()
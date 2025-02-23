

def parse_input():
    with open('input.txt') as f:
        lines = f.readlines()
        instructions = []
        for line in lines:
            line_list = line.split(',')
            if len(line_list) == 1:
                instructions.append(line_list[0].split())
            else:
                inst = line_list[0].split()
                inst.extend([line_list[1].strip()])
                instructions.append(inst)
        return instructions

def half(par, a, b):
    if par == "a":
        a = a // 2
    else:
        b = b // 2
    return a,b

def tpl(par, a, b):
    if par == "a":
        a *= 3
    else:
        b *= 3
    return a, b

def inc(par, a, b):
    if par == "a":
        a += 1
    else:
        b += 1
    return a, b

def main():
    instructions = parse_input()
    a = 1
    b = 0
    i = 0
    while i < len(instructions):
        inst = instructions[i]
        if inst[0] == "hlf":
            a, b = half(inst[1], a, b)
            i += 1
        elif inst[0] == "tpl":
            a, b = tpl(inst[1], a, b)
            i += 1
        elif inst[0] == "inc":
            a, b = inc(inst[1], a, b)
            i += 1
        elif inst[0] == "jmp":
            offset = int(inst[1])
            i += offset
        elif inst[0] == "jie":
            if inst[1] == "a" and a % 2 == 0:
                offset = int(inst[2])
                i += offset
            elif inst[1] == "b" and b % 2 == 0:
                offset = int(inst[2])
                i += offset
            else:
                i+=1
        elif inst[0] == "jio":
            if inst[1] == "a" and a == 1:
                offset = int(inst[2])
                i += offset
            elif inst[1] == "b" and b == 1:
                offset = int(inst[2])
                i += offset
            else:
                i += 1
    print(f"a = {a}, b = {b}")


if __name__ == '__main__':
    main()
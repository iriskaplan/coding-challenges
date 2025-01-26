import math


def parse_list():
    with (open('input.txt') as f):
        stones = [int(n) for n in f.readlines()[0].split()]
        return stones

def main():
    stones = parse_list()
    num_steps = 25
    current_stones = stones
    length = 0
    for s in current_stones:
        s_len = calculate_for_stone(s, num_steps)
        print(f"s = {s}, l = {s_len}")
        length += s_len
    print(length)


def calculate_for_stone(stone, num_steps):
    current_stones = [stone]
    for i in range(num_steps):
        temp = []
        for s in current_stones:
            if s == 0:
                temp.append(1)
            elif (math.floor(math.log(s, 10)) + 1) % 2 == 0:
                n = math.floor(math.log(s, 10)) + 1
                pad = 10 ** (n // 2)
                a, b = s // pad, s % pad
                temp.append(a)
                temp.append(b)
            else:
                new_num = s * 2024
                temp.append(new_num)
        print(f"i = {i}, l = {len(temp)}")
        current_stones = temp
    return len(current_stones)


if __name__ == '__main__':
    main()
import math


def parse_list():
    with (open('input.txt') as f):
        stones = [int(n) for n in f.readlines()[0].split()]
        return stones


def counts_dict(stones):
    d = dict()
    for s in stones:
        if s in d:
            d[s] += 1
        else:
            d[s]= 1
    return d


def main():
    stones = parse_list()
    num_steps = 75
    current_stones = counts_dict(stones)
    length = 0
    s_len = calculate_for_stones(current_stones, num_steps)
    length += s_len
    print(length)


def calculate_for_stones(stones, num_steps):
    current_stones = stones
    for i in range(num_steps):
        temp = dict()
        for s in current_stones:
            if s == 0:
                if 1 in temp:
                    temp[1] += 1 * current_stones[s]
                else:
                    temp[1] = 1 * current_stones[s]
            elif (math.floor(math.log(s, 10)) + 1) % 2 == 0:
                n = math.floor(math.log(s, 10)) + 1
                pad = 10 ** (n // 2)
                a, b = s // pad, s % pad
                if a in temp:
                    temp[a] += 1 * current_stones[s]
                else:
                    temp[a] = 1 * current_stones[s]
                if b in temp:
                    temp[b] += 1 * current_stones[s]
                else:
                    temp[b] = 1 * current_stones[s]
            else:
                new_num = s * 2024
                if new_num in temp:
                    temp[new_num] += 1 * current_stones[s]
                else:
                    temp[new_num] = 1 * current_stones[s]
        current_stones = temp
    return sum(current_stones.values())


if __name__ == '__main__':
    main()
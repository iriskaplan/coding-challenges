

def all_possible_subgroups():
    sub_groups = [[]]
    containers = [20, 15, 10, 5, 5]

    for c in containers:
        new_subs = []
        for group in sub_groups:
            with_c = group.copy()
            with_c.append(c)
            new_subs.append(with_c)
            new_subs.append(group)
        sub_groups = new_subs
    return sub_groups

def count_fit_eggnog(sub_group):
    count = dict()
    for group in sub_group:
        if sum(group) == 150:
            n = len(group)
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
    # for part 2
    minimal_k, minimal_v = 1000, 1000
    for n in count:
        if minimal_k > n:
            minimal_k = n
            minimal_v = count[minimal_k]
    return minimal_v

if __name__ == '__main__':
    all_g = all_possible_subgroups()
    print(count_fit_eggnog(all_g))
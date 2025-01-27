
def create_disk_array(disk_map):
    disk_array = []
    id = 0
    for i in range(0, len(disk_map), 2):
        files_count, free_count = int(disk_map[i]), int(disk_map[i + 1])
        for _ in range(files_count):
            disk_array.append(id)
        for _ in range(free_count):
            disk_array.append('.')
        id += 1
    return disk_array

def part1_checksum(disk_array):
    i, j = 0, len(disk_array) - 1
    while i < len(disk_array) and disk_array[i] != ".":
        i += 1

    while 0 < i < j < len(disk_array):
        disk_array[i], disk_array[j] = disk_array[j], disk_array[i]
        while i < len(disk_array) and disk_array[i] != ".":
            i += 1
        j -= 1
        while j > 0 and disk_array[j] == ".":
            j -= 1

    i = 0
    checksum = 0
    while i < len(disk_array) and disk_array[i] != ".":
        checksum += i * disk_array[i]
        i += 1
    return checksum


def resulting_checksum():
    with (open('input.txt') as f):
        disk_map = f.readlines()[0][:-1]
        disk_array = create_disk_array(disk_map)

        i, j = 0, len(disk_array) - 1

        while i < len(disk_array) and disk_array[i] != ".":
            i += 1

        l = i
        while l == "." and l < len(disk_array):
            l += 1

        k = len(disk_map) - 2
        amount_j = int(disk_map[k])
        amount_i = int(disk_map[1])

        while 0 < i < j < len(disk_array):
            if amount_i >= amount_j:
                for _ in range(amount_j):
                    disk_array[i], disk_array[j] = disk_array[j], disk_array[i]

            # else:

        # idea: for each file from the end find the first vacant space that I can fit it in and move it there
        # if i cant find, continue
        while 0 < j < len(disk_array):
            disk_array[i], disk_array[j] = disk_array[j], disk_array[i]
            while i < len(disk_array) and disk_array[i] != ".":
                i += 1
            j -= 1
            while j > 0 and disk_array[j] == ".":
                j -= 1

        i = 0
        checksum = 0
        while i < len(disk_array) and disk_array[i] != ".":
            checksum += i * disk_array[i]
            i += 1
        return checksum





if __name__ == '__main__':
    print(resulting_checksum())
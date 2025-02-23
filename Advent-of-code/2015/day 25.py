

def find_code():
    ci, cj = 1,1
    max_i = 1
    code = 20151125
    while True:
        if ci == 1:
            max_i += 1
            ci = max_i
            cj = 1
        else:
            ci -= 1
            cj += 1
        code *= 252533
        code = code % 33554393
        if ci == 100 and cj == 100:
            print(f"(i, j) = {ci, cj}, code = {code}")
            break

find_code()
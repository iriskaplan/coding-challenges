
import math


def main():
    n = 3
    gifts = 0
    gifts_count = 200
    presents_to_house = 11
    while gifts < gifts_count:
        gifts = 0
        i = 1
        while i <= math.sqrt(n):
            if n % i == 0:
                if n / i == i and n <= 50 * i:
                    gifts += i * presents_to_house
                else:
                    if n <= 50 * i:
                        gifts += (i * presents_to_house)
                    if n <= 50 * int((n/i)):
                        gifts += (n/i)*presents_to_house
            i += 1
        n += 1
    print(n-1)


if __name__ == '__main__':
    main()
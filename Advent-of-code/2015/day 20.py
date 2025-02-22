
import math


def main():
    n = 3
    gifts = 0
    gifts_count = 120
    while gifts < gifts_count:
        gifts = 0
        i = 1
        while i <= math.sqrt(n):
            if n % i == 0:
                if n / i == i:
                    gifts += i * 10
                else:
                    gifts += (i * 10) + (n/i)*10
            i += 1
        n += 1
    print(n-1)



if __name__ == '__main__':
    main()
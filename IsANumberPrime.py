import math


def is_prime(num):
    if num < 2:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    length = int(math.sqrt(num)) + 1
    for i in range(3, length, 2):
        if num % i == 0:
            return False

    return True


if __name__ == "__main__":
    print(is_prime(4))
    # print(is_prime(1))
    # print(is_prime(2))
    # print(is_prime(-1))
    # print(is_prime(73))
    # print(is_prime(75))

import math


def narcissistic(value):
    text = str(value)
    length = len(text)

    temp = 0
    for char in text:
        temp = temp + math.pow(int(char), length)

    return temp == value


if __name__ == "__main__":
    print(narcissistic(7))
    print(narcissistic(371))
    print(narcissistic(122))
    print(narcissistic(4887))

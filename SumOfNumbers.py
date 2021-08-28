
def get_sum(a,b):
    if a == b:
        return a
    sum = 0
    for i in range(min(a, b), max(a, b) + 1, 1):
        sum += i
    return sum


if __name__ == "__main__":
    print(get_sum(1, 3))


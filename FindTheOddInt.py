def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 != 0:
            return num
    return None

def find_it2(seq):
    if len(seq) == 1:
        return seq[0]

    dups = dict()

    for num in seq:
        if num in dups:
            dups[num] = dups[num] + 1
        else:
            dups[num] = 1
    print(dups)

    for key, value in dups.items():
        if isOdd(value):
            return key

    return None


def isOdd(number):
    return number % 2 != 0


if __name__ == "__main__":
    print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))

def max_sequence(arr):
    if len(arr) == 0:
        return 0

    l = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            l.append(sum(arr[i:j + 1]))
    return max(max(l), 0) if len(arr) != 0 else 0


if __name__ == "__main__":
    # print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    # print(max_sequence([-2, 11, -3, -4, 3, 2, 21, -25, -1, 0, 1]))
    # print(max_sequence([-2, -11, -3, -1, -5]))
    print(max_sequence([4, 36, 37, 39, 7, 10, 11, 44, 43]))
    print(max_sequence([1, 2, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22, 24, 25, 28, 29]))
    print(max_sequence([1, 3, 4, 6, 7, 8, 9, 10, 11, 12, 15, 16, 22, 24, 27, 29, -1]))

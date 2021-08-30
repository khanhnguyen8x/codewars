def move_zeros(arrays):
    write_pointer = 0
    length = len(arrays)

    for read_pointer in range(length):
        if arrays[read_pointer] != 0:
            arrays[write_pointer] = arrays[read_pointer]
            write_pointer = write_pointer + 1

    for i in range(write_pointer, length):
        arrays[i] = 0

    return arrays


if __name__ == "__main__":
    array = [1, 0, 1, 2, 0, 1, 3];
    move_zeros(array)

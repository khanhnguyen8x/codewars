def increment_string(strng):
    head = strng.rstrip("1234567890")
    tail = strng[len(head):]
    if len(tail) == 0:
        return head + "1"
    return head + str(int(tail) + 1).zfill(len(tail))


if __name__ == "__main__":
    inp = str(input())
    print(increment_string(inp))

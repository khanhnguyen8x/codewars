def digital_root(n: int):
    if len(str(n)) == 1:
        return n
    return calculate(str(n))


def calculate(text: str):
    total = 0
    if len(text) > 1:
        for char in text:
            total = total + int(char)

    if len(str(total)) > 1:
        return calculate(str(total))

    return total


if __name__ == "__main__":
    print(digital_root(16))
    print(digital_root(942))
    print(digital_root(132189))
    print(digital_root(493193))

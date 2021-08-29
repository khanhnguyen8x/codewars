def rgb(r, g, b):
    return '{:02X}{:02X}{:02X}'.format(getValue(r), getValue(g), getValue(b))


def getValue(color):
    if color < 0:
        color = 0
    if color > 255:
        color = 255
    return color


if __name__ == "__main__":
    print(rgb(0, 0, 0))
    print(rgb(1, 2, 3))
    print(rgb(255, 255, 255))
    print(rgb(-20, 275, 125))

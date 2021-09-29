def get_string_numeric(strng):
    numeric = ""
    if strng.isnumeric():
        return strng
    for i in range(-1, 0-len(strng), -1):
        if strng[i].isnumeric():
            numeric = strng[i] + numeric
        else:
            break
    return numeric

def get_string_alpha(strng, numeric):
    return strng[0:len(strng) - len(numeric)]

def increment_string(strng):
    if len(strng) == 0:
        return "1"

    numeric = get_string_numeric(strng)
    # print(f"numeric: {numeric}")
    len_numeric = len(numeric)
    if len_numeric == 0:
        return strng + "1"

    alpha = get_string_alpha(strng, numeric)
    # print(f"alpha: {alpha}")

    num = int(numeric)
    len_num_before = len(str(num))
    # print(f"num: {num}")
    num = num + 1
    len_num_after = len(str(num))

    # print(f"len_numeric: {len_numeric}")
    # print(f"len_num_before: {len_num_before}")
    # print(f"len_num_after: {len_num_after}")

    if len_numeric >= len_num_before:
        if len_numeric == len_num_after:
            strng = alpha + str(num)
        elif len_numeric > len_num_after:
            diff = len_numeric - len_num_after
            temp = ""
            for i in range(diff):
                temp = temp + "0"
            strng = alpha + temp + str(num)
        elif len_numeric < len_num_after:
            strng = alpha + str(num)

    return strng


if __name__ == "__main__":
    inp = str(input())
    print(increment_string(inp))


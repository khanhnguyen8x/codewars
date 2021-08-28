def duplicate_count(text):
    seen = set()
    dups = set()

    for char in text:
        char = char.lower()
        if char not in seen:
            seen.add(char)
        else:
            dups.add(char)
    return len(dups)

def duplicate_count2(text):
    # Your code goes here
    if len(text) == 0:
        return 0

    text = text.lower()
    temp = ''
    for str in text:
        if str not in temp:
            temp = temp + str

    count = 0

    for str1 in temp:
        counting = 0

        for str2 in text:
            if str1 == str2:
                counting = counting + 1

        if counting > 1:
            count = count + 1

    return count


if __name__ == "__main__":
    print(duplicate_count("abcde"))
    print(duplicate_count("aabbcde"))
    print(duplicate_count("aabBcde"))
    print(duplicate_count("indivisibility"))
    print(duplicate_count("Indivisibilities"))
    print(duplicate_count("aA11"))
    print(duplicate_count("aA11"))

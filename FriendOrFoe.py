def friend(x):
    if len(x) == 0:
        return []
    result = []
    for item in x:
        if len(item) == 4:
            result.append(item)

    return result

if __name__ == "__main__":
    input =  ["Ryan", "Kieran", "Jason", "Yous"]
    result = friend(input)
    print(result)

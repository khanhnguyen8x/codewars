def filter_list(l):
    result = []
    for item in l:
        if not isinstance(item, str):
            result.append(item)
    return result


if __name__ == "__main__":
    print(filter_list([1, 2, 'a', 'b']))
    print(filter_list([1, 'a', 'b', 0, 15]))
    print(filter_list([1, 2, 'aasf', '1', '123', 123]))

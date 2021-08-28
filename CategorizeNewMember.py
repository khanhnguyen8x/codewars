def open_or_senior(data):
    result = []
    for item in data:
        if item[0] >= 55 and item[1] > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result


if __name__ == "__main__":
    print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))
    print(open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)]))
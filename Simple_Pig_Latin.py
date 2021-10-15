def pig_it(text):
    result = ""
    texts = text.split(" ")
    for text in texts:
        if text.isalpha():
            text = text[1:] + text[0] + "ay"
            result += text
            result += " "
        else:
            result += text
            result += " "
    return result.strip()


if __name__ == "__main__":
    print(pig_it("Pig latin is cool"))
    print(pig_it("Hello world !"))